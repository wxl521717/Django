#coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator

def index(request):
    #查询每个分类最新的4条、最热的4条数据
    typelist = TypeInfo.objects.all()
    type0 = typelist[0].goodinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodinfo_set.order_by('-gclick')[0:4] 
    type2 = typelist[2].goodinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodinfo_set.order_by('-gclick')[0:4]   
    type5 = typelist[5].goodinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodinfo_set.order_by('-gclick')[0:4]
    context = {'title':'首页','guest_cart':1,
                'type0':type0,'type01':type01,
                'type1':type1,'type11':type11,
                'type2':type2,'type21':type21,
                'type3':type3,'type31':type31,
                'type4':type4,'type41':type41,
                'type5':type5,'type51':type51, }

    return render(request,'df_goods/index.html',context)


def list(request,typeid,pageid,sort):
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    news = typeinfo.goodinfo_set.order_by('-id')[:2]
    if sort=='1':
        good_list = GoodInfo.objects.filter(gtype_id=int(typeid)).order_by('-id')
    elif sort =='2':
        good_list = GoodInfo.objects.filter(gtype_id=int(typeid)).order_by('-gprice')
    elif sort=='3':
        good_list = GoodInfo.objects.filter(gtype_id=int(typeid)).order_by('-gclick')

    paginator = Paginator(good_list,10)
    page = paginator.page(int(pageid))
    context = {'title':typeinfo.ttitle,'guest_cart':1,
                'page':page,
                'paginator':typeinfo,
                'sort':sort,
                'news':news
    }
    return render(request,'df_goods/list.html',context)

def detail(request,id):
    goods = GoodInfo.objects.get(pk=int(id))
    goods.gclick=goods.gclick+1
    goods.save()
    news = goods.gtype.goodinfo_set.order_by('-id')[0:2]
    context = {'title':goods.gtype.ttitle,'guest_cart':1,
                'g':goods,'news':news,'id':id}
    return render(request,'df_goods/detail.html',context)











