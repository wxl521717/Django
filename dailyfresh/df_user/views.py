#coding=utf-8
from django.shortcuts import render,redirect
from models import *
import hashlib 
from django.http import JsonResponse,HttpResponseRedirect

def register(request):
    return render(request,'df_user/register.html')

def register_handle(request):

    #接受用户输入
    post = request.POST 
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    #密码两次验证
    if upwd != upwd2:
        return redirect('/user/register/')

    #加密
    sl = hashlib.sha1()
    sl.update(upwd.encode('utf-8'))
    upwd3 = sl.hexdigest()
    #创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    #注册成功转到登陆页面
    return redirect('/user/login/')


def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)

def login_handle(request):
    #接受请求消息
    uname = request.POST.get('username')
    upwd = request.POST.get('pwd')
    jizhu = request.POST.get('jizhu',0)
    #根据用户名查询对象
    users = UserInfo.objects.filter(uname=uname)
    print uname

    #判断：如果未查到则用户名出错，如果查到则判断密码是否正确，正确则转到用户中心。
    if len(users)==1:
        sl= hashlib.sha1()
        sl.update(upwd.encode('utf-8'))
        if sl.hexdigest() ==users[0].upwd:
            red = HttpResponseRedirect('/user/info')
            #记住用户名
            if jizhu !=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id']=users[0].id
            request.session['user_name']=uname
            return red

        else:
            context = {'title':'用户登录','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
            return render(request,'df_user/login.html',context)
    else:
        context = {'title':'用户登录','error_name':1,'error_pwd':0,'uname':uname,'upwd':upwd}
        return render(request,'df_user/login.html',context)

#用户中心
def info(request):
    user_email = UserInfo.objects.get(id = request.session['user_id']).uemail
    context = {
        'title':'用户中心',
        'user_email':'user_email',
        'user_name':request.session['user_name']}
    return render(request,'df_user/user_center_info.html',context)

def order(request):
    context = {'title':'用户中心'}
    return render(request,'df_user/user_center_order.html',context)

def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method=='POST':
        user.urecv=request.POST.get('urecv')
        user.uaddress=request.POST.get('uaddress')
        user.upostcode=request.POST.get('upostcode')
        user.uphone=request.POST.get('uphone')
        user.save()
    context={'title':'用户中心','user':user}
    return render(request,'df_user/user_center_site.html',context)














