from django.contrib import admin
from .models import Post #从models模块中导入Post模型

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date') #设置admin后台,Post类的显示外观

admin.site.register(Post,PostAdmin)

#admin.site.register(Post) #通过注册把Post纳入后台管理