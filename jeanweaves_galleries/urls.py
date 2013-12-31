# -*- coding: utf-8 -*-


from django.conf.urls import patterns
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView


urlpatterns = patterns('',
    url(r'^$', 'jeanweaves_galleries.views.index', name='index'),
    url(r'^animals/$', 'jeanweaves_galleries.views.animals', name='animals'),
    url(r'^damask/$', 'jeanweaves_galleries.views.damask', name='damask'),
    url(r'^placemats-and-napkins/$', 'jeanweaves_galleries.views.placemats_and_napkins', name='placemats_and_napkins'),
    url(r'^runners/$', 'jeanweaves_galleries.views.runners', name='runners'),
    url(r'^scarves/$', 'jeanweaves_galleries.views.scarves', name='scarves'),
    url(r'^throws/$', 'jeanweaves_galleries.views.throws', name='throws'),
    url(r'^towels/$', 'jeanweaves_galleries.views.towels', name='towels'),
    url(r'^portfolio/$', 'jeanweaves_galleries.views.portfolio', name='portfolio'),

    # Backward compat with old URLs:
    (r'^index\.html$', RedirectView.as_view(url=reverse_lazy('index'))),
    (r'^animals\.html$', RedirectView.as_view(url=reverse_lazy('animals'))),
    (r'^damask\.html$', RedirectView.as_view(url=reverse_lazy('damask'))),
    (r'^placemats-and-napkins\.html$', RedirectView.as_view(url=reverse_lazy('placemats_and_napkins'))),
    (r'^runners\.html$', RedirectView.as_view(url=reverse_lazy('runners'))),
    (r'^scarves\.html$', RedirectView.as_view(url=reverse_lazy('scarves'))),
    (r'^throws\.html$', RedirectView.as_view(url=reverse_lazy('throws'))),
    (r'^towels\.html$', RedirectView.as_view(url=reverse_lazy('towels'))),
)
