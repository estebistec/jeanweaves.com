# -*- coding: utf-8 -*-


from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('',
    url(r'', include('jeanweaves_public.urls')),
    url(r'', include('jeanweaves_galleries.urls')),
    url(r'', include('jeanweaves_blog.urls')),
)
