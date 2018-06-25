# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Post
from comments.models import Comment
from django import forms
from categories.models import Category


def post(request, post_id):

    this_post = get_object_or_404(Post, id=post_id)
    comment_list = []
    comments = Comment.objects.all().filter(post_id=post_id)
    for comm in comments:
        comment_list += comments.all().filter(comments=comm).order_by('-created')
    context = {
        'post': this_post,
        'comments': comment_list,
    }
    return render(request, "post.html", context)


class MakePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = 'name', 'categories', 'content'


def make_post(request):

    if request.method == 'GET':
        form = MakePostForm()
        return render(request, "make_post.html", {'form': form})
    elif request.method == 'POST':
        form = MakePostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post = Post(name=data['name'], content=data['content'])
            post.author = request.user
            post.save()
            categories = []
            for i in data['categories']:
                categories.append(Category.objects.get(name=i))
            post.categories = categories
            return redirect('post', post_id=post.id)
        else:
            return render(request, "make_post.html", {'form': form})


def editing_post(request, post_id):

    this_post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'GET':
        form = MakePostForm(instance=this_post)
        return render(request, "editing_post.html", {'form': form, 'post': this_post})
    elif request.method == 'POST':
        form = MakePostForm(request.POST, instance=this_post)
        if form.is_valid():
            post = form.save()
            return redirect('post', post_id=post.id)
        else:
            return render(request, "editing_post.html", {'form': form, 'post': this_post})
