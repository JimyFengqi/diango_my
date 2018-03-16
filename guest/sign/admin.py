from django.contrib import admin
from sign.models import Event,Guest

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['name','status','address','start_time','id']#显示列表
    search_fields=['name']#搜索栏
    list_filter=['status']#过滤器

class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','create_time','event','id']#显示列表
    search_fields=['realname']#搜索栏
    list_filter=['sign']#过滤器
    
admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)