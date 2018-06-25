# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import login
from core.models import User


class RegistrationForm(forms.Form):

    name = forms.CharField(min_length=3, max_length=30, label='Name')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')


def reg(request):

    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['name']
            my_password = data['password']
            User.objects.create_user(username=username, password=my_password)
            authenticate(username=username, password=my_password)
            return redirect('profile')
        else:
            return render(request, 'registration.html', {'form': form})
