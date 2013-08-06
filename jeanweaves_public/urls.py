# -*- coding: utf-8 -*-


from django.conf.urls import patterns
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView


urlpatterns = patterns('',
    url(r'^about/$', 'jeanweaves_public.views.about', name='about'),
    url(r'^contact/$', 'jeanweaves_public.views.contact', name='contact'),
    url(r'^exhibits/$', 'jeanweaves_public.views.exhibits', name='exhibits'),

    # Backward compat with old URLs:
    (r'^about\.html$', RedirectView.as_view(url=reverse_lazy('about'))),
    (r'^contact\.html$', RedirectView.as_view(url=reverse_lazy('contact'))),
    (r'^exhibits\.html$', RedirectView.as_view(url=reverse_lazy('exhibits'))),
)
