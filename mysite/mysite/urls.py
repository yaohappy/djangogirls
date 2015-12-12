from django.conf.urls import *
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
)

urlpatterns += patterns('trips.views',
    url(r'^$', 'home'),
    url(r'^hello/$', 'hello_world'),
    url(r'^post/(?P<idx>\d+)/$', 'post_detail', name='post_detail'),
    url(r'^search/$', 'search')
)