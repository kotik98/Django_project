# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from categories.models import Category


class Post(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='author', verbose_name='Автор')
    categories = models.ManyToManyField(Category, blank=True, related_name='categories', verbose_name='Категории')
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    is_archive = models.BooleanField(default=False)

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'
        ordering = 'name', 'author',

    def __unicode__(self):
        return self.name


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
