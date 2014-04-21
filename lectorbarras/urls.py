from django.conf.urls import patterns, url, include
from lectorbarras import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^getprice/$', views.getprice, name='getprice'),
)