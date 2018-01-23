#coding=utf-8
from django.db import models

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    urecv = models.CharField(max_length=20,default='')      #收件人
    uaddress = models.CharField(max_length=100,default='')   
    upostcode = models.CharField(max_length=6,default='')   #邮编
    uphone = models.CharField(max_length=11,default='')