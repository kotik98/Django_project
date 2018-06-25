# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import LogoutView


class Logout(LogoutView):

    template_name = 'logout.html'

    def logout(self):
        return super(self.request)
