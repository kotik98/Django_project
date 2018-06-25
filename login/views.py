# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, HttpResponse, reverse
from django import forms
from django.contrib.auth.views import LoginView


class Login(LoginView):

    template_name = 'login.html'

    def get_success_url(self):
        return reverse('profile')
