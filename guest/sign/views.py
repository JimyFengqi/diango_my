from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse,HttpResponseRedirect
#导入django自带的鉴权模块
from django.contrib import auth
#导入login_required模块，来限制某个视图，加入这个模块之后，必须登录之后才能显示
from django.contrib.auth.decorators import login_required
#导入由sign.models里面创建的实体类内容
from sign.models import Event,Guest
#导入分页显示相关类，参数
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



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
    event_list = Event.objects.all()
    #采用cookies的方式读取浏览器的数据
    #username = request.COOKIES.get('user','')
    #通过session的方式读取浏览器数据
    username=request.session.get("user",'')
    return render(request,"event_manage.html",{"user":username,"events":event_list})
    
@login_required
def guest_manage(request):
    username=request.session.get("user","")
    #获取其全部的实体内容，即获得所有guest
    guest_list=Guest.objects.all()
    #对嘉宾进行分页显示，每一页显示3个人
    paginator=Paginator(guest_list,2)
    page=request.GET.get('page')
    try:
        contacts=paginator.page(page)
    except PageNotAnInteger:
        #如果page不是一个整数，先显示第一页
        contacts = paginator.page(1)
    except EmpyPage:
        #如果page的页数超出做大值（9999），显示最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request,"guest_manage.html",{"user":username,"guests":contacts})
  
#查询方法    
@login_required
def search_event_name(request):
    username=request.session.get("user","")
    search_event_name=request.GET.get("name","")
    event_list=Event.objects.filter(name=search_event_name)
    return render(request,"event_manage.html",{"user":username,"events":event_list})
    
@login_required
def search_guest_name(request):
    username=request.session.get("user","")
    search_guest_name=request.GET.get("realname","")
    guest_list=Guest.objects.filter(realname=search_guest_name)
    return render(request,"guest_manage.html",{"user":username,"guests":guest_list})

    
#签到页面的控制方法
@login_required
def sign_index(request,event_id):
    event = get_object_or_404(Event,id=event_id)
    return render(request,"sign_index.html",{'event':event})
#签到动作的控制方法
@login_required
def sign_index_action(request,event_id):
    event = get_object_or_404(Event,id=event_id)
    phone=request.POST.get('phone','')
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'phone error.'})
        
    result=Guest.objects.filter(phone=phone,event_id=event_id)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'event_id or phone error.'})
        
    result=Guest.objects.get(phone=phone,event_id=event_id)
    if result.sign:
        return render(request,'sign_index.html',{'event':event,'hint':'user has sign in.'})
    else:
        Guest.objects.filter(phone=phone,event_id=event_id).update(sign='1')
        return render(request,'sign_index.html',{'event':event,'hint':'sign insuccess','guest':result})
#退出方法
@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')       

        