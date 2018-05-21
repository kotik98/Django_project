from django.conf.urls import include, url

from posts import views

urlpatterns = [

    url(r'^new_post/$', views.make_post, name='new_post'),
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post'),
    url(r'^posts/$', views.posts_list, name='posts_list'),
]
