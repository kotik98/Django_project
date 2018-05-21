# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name='Имя')

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'
        ordering = 'name',

    def __unicode__(self):
        return self.name
