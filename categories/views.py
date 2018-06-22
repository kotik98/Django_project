# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Category
from posts.models import Post
from django import forms


class CategoriesListForm(forms.Form):

    sort = forms.ChoiceField(choices=(
        ('name', 'Name asc'),
        ('-name', 'Name desc'),
        ('id', 'ID'),
    ), required=False)
    search = forms.CharField(required=False)


def category_detail(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    context = {
        'category': category,
        'posts': Post.objects.all().filter(categories=category_id)
    }

    return render(request, 'category_detail.html', context)


def categories_list(request):

    categories = Category.objects.all()
    form = CategoriesListForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        if data['sort']:
            categories = categories.order_by(data['sort'])
        if data['search']:
            categories = categories.filter(name__icontains=data['search'])
    context = {
        'categories': categories,
        'categories_form': form,
    }
    return render(request, 'categories_list.html', context)
