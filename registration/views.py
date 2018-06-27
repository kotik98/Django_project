# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django import forms
from core.models import User
from django.views.generic import CreateView


class RegistrationForm(forms.ModelForm):
    Username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), label="", min_length=3,
                               max_length=30)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('Username', 'email', 'password1', 'password2')

    def clean_Username(self):
        for u in User.objects.all():
            if u.username == self.cleaned_data.get("Username"):
                raise forms.ValidationError("this name is already taken")
        return self.cleaned_data.get("Username")

    def clean_email(self):
        for u in User.objects.all():
            if u.email == self.cleaned_data.get("email"):
                raise forms.ValidationError("this email is registered by the user")
        return self.cleaned_data.get("email")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data["Username"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class RegistrationView(CreateView):
    form_class = RegistrationForm
    success_url = 'profile'
    model = User
    template_name = 'registration.html'

    def get_success_url(self):
        return reverse('profile')
