# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from core.models import User
from django.views.generic import UpdateView, CreateView


class UserProfile(CreateView):

    model = User
    fields = 'username', 'bio', 'birth_date',
    context_object_name = 'user'
    template_name = 'user_profile.html'
