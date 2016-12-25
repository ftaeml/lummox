from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<id>\d+)?$', views.post, name="post"),
    url(r'^comment/(?P<id>\d+)?$', views.comment, name="comment"),
]