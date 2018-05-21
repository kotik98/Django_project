
from categories import views as categories_views
from django.conf.urls import include, url


urlpatterns = [

    url(r'^$', categories_views.categories_list, name='categories'),
    url(r'^(?P<category_id>\d+)/$', categories_views.category_detail, name='category_detail'),
]
