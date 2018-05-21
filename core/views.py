# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


def index(response):

    name = response.GET.get('name')
    return HttpResponse('Hello {}, this is main page'.format(name))
