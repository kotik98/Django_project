# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from categories.models import Category
from posts.models import Post


def index(request):

    categories = Category.objects.all().order_by('?')[:10]
    posts = Post.objects.all().order_by('created')[:10]
    user = request.user
    context = {
        'categories': categories,
        'posts': posts,
        'user': user
    }
    return render(request, "index.html", context)
