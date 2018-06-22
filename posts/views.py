# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from comments.models import Comment


def post(request, post_id):

    comment_list = []
    comments = Comment.objects.all().filter(post_id=post_id)
    for comm in comments:
        comment_list += comments.all().filter(comments=comm).order_by('-created')
    this_post = get_object_or_404(Post, id=post_id)
    context = {
        'post': this_post,
        'comments': comment_list,
    }
    return render(request, "post.html", context)

def posts_list(request):

    return HttpResponse('This is pots page')

def make_post(request):

    return HttpResponse('This is make post page')