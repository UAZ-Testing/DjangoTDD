from django.conf.urls import url
from django.contrib import admin
from lists import views
from lists import urls as list_urls

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(?P<list_id>\d+)/$', views.view_list, name='view_list'),
]


