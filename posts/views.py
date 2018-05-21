# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post, Comment


def post(request, post_id):

    comments = Comment.objects.get(post=post_id)
    this_post = Post.objects.get(id=post_id)
    context = {
        'post': this_post,
        'comments': comments,
    }
    return render(request, "post.html", context)

def posts_list(request):

    return HttpResponse('This is pots page')

def make_post(request):

    return HttpResponse('This is make post page')