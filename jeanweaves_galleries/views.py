# -*- coding: utf-8 -*-


from django.utils.translation import ugettext_lazy as _
from django.views.decorators.cache import cache_page

from . import galleries
from jeanweaves_public.views import JeanWeavesPageView


class JeanWeavesGalleryView(JeanWeavesPageView):
    page_layout = 'jeanweaves_galleries/_layout.html'
    photos = []

    def get_page_context(self):
        page_context = super(JeanWeavesGalleryView, self).get_page_context()
        page_context['photos'] = self.photos
        return page_context


index = JeanWeavesGalleryView.as_view(
    template_name='jeanweaves_galleries/index.html',
    photos=galleries.index
)

animals = JeanWeavesGalleryView.as_view(
    template_name='jeanweaves_galleries/animals.html',
    page_title=_('Animals'),
    photos=galleries.animals
)

damask = JeanWeavesGalleryView.as_view(
    template_name='jeanweaves_galleries/damask.html',
    page_title=_('Damask'),
    photos=galleries.damask
)

placemats_and_napkins = JeanWeavesGalleryView.as_view(
    template_name='jeanweaves_galleries/placemats-and-napkins.html',
    page_title=_('Placemats and Napkins'),
    photos=galleries.placemats_and_napkins
)

runners = JeanWeavesGalleryView.as_view(
    template_name='jeanweaves_galleries/runners.html',
    page_title=_('Runners'),
    photos=galleries.runners
)

scarves = JeanWeavesGalleryView.as_view(
    template_name='jeanweaves_galleries/scarves.html',
    page_title=_('Scarves'),
    photos=galleries.scarves
)

throws = JeanWeavesGalleryView.as_view(
    template_name='jeanweaves_galleries/throws.html',
    page_title=_('Throws'),
    photos=galleries.throws
)

towels = JeanWeavesGalleryView.as_view(
    template_name='jeanweaves_galleries/towels.html',
    page_title=_('Towels'),
    photos=galleries.towels
)

THIRTY_DAYS = 60 * 60 * 24 * 30
index = cache_page(THIRTY_DAYS)(index)
animals = cache_page(THIRTY_DAYS)(animals)
damask = cache_page(THIRTY_DAYS)(damask)
placemats_and_napkins = cache_page(THIRTY_DAYS)(placemats_and_napkins)
runners = cache_page(THIRTY_DAYS)(runners)
scarves = cache_page(THIRTY_DAYS)(scarves)
throws = cache_page(THIRTY_DAYS)(throws)
towels = cache_page(THIRTY_DAYS)(towels)
