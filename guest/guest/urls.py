"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path,re_path
from sign import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #加入view视图窗口，其中第一个参数，index是网址上面的访问地址，第二个参数是view.py中定义的控制方法
    #也就是说，通过views.index能够调用view.py里面定义的的index方法来控制index页面的显示内容
    path('index/',views.index),

    #添加登录界面与方法
    path('login_action/',views.login_action),
    #添加event_manage界面与方法
    path('event_manage/',views.event_manage),
    path('guest_manage/',views.guest_manage),
    #访问已经定义好的页面，如果没有登录，都会跳转到index页面
    path('accounts/login',views.index),
    #添加搜索页面以及其方法
    path('search_event_name/',views.search_event_name),
    path('search_guest_name/',views.search_guest_name),

    #添加签到页面,含有正则表达是的，不需要通过re_path或者url的方式将其加入进来
    re_path(r'^sign_index/(?P<event_id>[0-9]+)',views.sign_index),
    #url('sign_index/(?P<event_id>[0-9]+/)',views.sign_index),
    re_path('sign_index_action/(?P<event_id>[0-9]+)',views.sign_index_action),
    #url(r'^sign_index_action/(?P<event_id>[0-9]+/)',views.sign_index_action),
    
    path('logout/',views.logout),
    
]
