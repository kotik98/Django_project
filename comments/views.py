# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from posts.models import Post
from django.shortcuts import render


def make_comment(request, post_id):

    return render(request, reversed(Post.objects.get(id=post_id)), {})
