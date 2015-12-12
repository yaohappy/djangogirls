# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', home),
	url(r'^hello/$', hello_world),
    url(r'^post/(?P<idx>\d+)/$', post_detail, name='post_detail'),
    url(r'^search/$', search),
]