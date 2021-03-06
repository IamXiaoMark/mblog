from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template.loader import get_template
from datetime import datetime

# Create your views here.
def homepage(request):
    # posts = Post.objects.all() #获取所有数据项
    # post_lists = list()
    # for count, post in enumerate(posts):
    #     post_lists.append("No.{}:".format(str(count)) + str(post) +"<br>")
    #     post_lists.append("<small>" + str(post.body.encode('utf-8'))+"</small><br><br>")
    # return HttpResponse(post_lists) #通过HttpResposene输出到网页中

    template = get_template('index.html')
    posts = Post.objects.all()

    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)