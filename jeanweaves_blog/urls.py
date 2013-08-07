# -*- coding: utf-8 -*-


from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('',
    url(r'^blog/$', 'jeanweaves_blog.views.posts', name='posts'),
)
