# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Category


def category_detail(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    context = {
        'category': category,
        'posts': category.posts.all().filter(is_archive=False)
    }

    return render(request, 'category_detail.html', context)


def categories_list(request):

    context = {
        'categories': Category.objects.all()
    }

    return render(request, 'categories_list.html', context)
