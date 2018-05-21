"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from core.views import index
from django.conf import settings
from django.conf.urls import include, url
from usr_profile.views import user_profile
from login.views import login
from logout.views import logout
from registration.views import reg

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', index),

    url(r'^categories/', include('categories.urls')),

    url(r'^profile/(\w+)', user_profile),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^registration/$', reg),

    url(r'', include('posts.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
