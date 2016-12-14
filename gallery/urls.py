from django.conf.urls import url
from django.contrib import admin
from gallery import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.gallery, name='gallery'),
    url(r'^photos/$', views.album_single, name="album_single"),
    url(r'^album_two/$', views.album_two, name="album_two"),
    url(r'^upload/$', views.upload, name="upload"),
#    url(r'^about', views.about, name='about'),
#    url(r'^blog', views.blog, name='blog'),
#    url(r'^blog_2004', views.blog_2004, name='blog_2004'),
#    url(r'^contact', views.contact, name='contact'),
#    url(r'^portfolio_one', views.portfolio_one, name='portfolio_one'),
#    url(r'^portfolio_two', views.portfolio_two, name='portfolio_two'),
]