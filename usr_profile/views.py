# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def user_profile(response, name):

    return HttpResponse('this is user {}'.format(name))
