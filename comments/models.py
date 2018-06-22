# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from posts.models import Post
from django.db import models
from django.conf import settings


class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', verbose_name='Автор')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, related_name='post', verbose_name='Пост ')
    comment = models.ForeignKey('self', blank=True, null=True, related_name='comments')

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        ordering = 'created', 'id'

