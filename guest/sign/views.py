from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
#导入django自带的鉴权模块
from django.contrib import auth
#导入login_required模块，来限制某个视图，加入这个模块之后，必须登录之后才能显示
from django.contrib.auth.decorators import login_required

# 创建第一个主视图，即登录视图
def index(request):
    #return HttpResponse("hello,world!")
    return render(request,"index.html")


'''
#定义点击下登录按钮的动作
def login_action(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        
        if username == 'admin' and password == 'admin123':
            response =  HttpResponseRedirect("/event_manage/")
            #采用cookie的方式进行数据传递
            #response.set_cookie('user',username,3600)
            #采取session的方式传递数据
            request.session['user']=username
            return response
        else:
            return render(request,'index.html',{'error':"username or password error! %s"})
    else:
        return render(request,'index.html',{'error':"username or password error! %s"})
 '''    
def login_action(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        #通过自带的鉴权模块来识别用户信息
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            response =  HttpResponseRedirect("/event_manage/")
            #采用cookie的方式进行数据传递
            #response.set_cookie('user',username,3600)
            #采取session的方式传递数据
            request.session['user']=username
            return response
        else:
            return render(request,'index.html',{'error':"username or password error! %s"})
    else:
        return render(request,'index.html',{'error':"username or password error! %s"})        
#这个event_manage 页面必须登陆之后才能显示    
@login_required       
def event_manage(request):
    #采用cookies的方式读取浏览器的数据
    #username = request.COOKIES.get('user','')
    #通过session的方式读取浏览器数据
    username=request.session.get("user",'')
    return render(request,"event_manage.html",{"user":username})