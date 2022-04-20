# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Post

# def index(request):
#     return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    template = loader.get_template('post.html')
    context = {
        'post' : post,
        }
    return HttpResponse(template.render(context, request))



def blog(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    template = loader.get_template('blog.html')
    context = {
        'latest_post_list': latest_post_list,
    }
    return HttpResponse(template.render(context, request))
