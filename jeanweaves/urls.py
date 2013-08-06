# -*- coding: utf-8 -*-


from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    url(r'', include('jeanweaves_public.urls')),
    url(r'', include('jeanweaves_galleries.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
