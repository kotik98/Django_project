from django.conf.urls import include, url

from posts import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^new_post/$', login_required(views.make_post), name='new_post'),
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post'),
    url(r'^editing_post/(?P<post_id>\d+)/$', login_required(views.editing_post), name='editing_post'),
]
