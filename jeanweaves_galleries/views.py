# -*- coding: utf-8 -*-


from django.utils.translation import ugettext_lazy as _
from django.views.decorators.cache import cache_page

from . import galleries
from jeanweaves_public.views import JeanWeavesPageView


class JeanWeavesGalleryView(JeanWeavesPageView):
    page_layout = 'jeanweaves_galleries/_layout.html'
    page_scripts = [
        'js/vendor/zepto.min.js',
        'js/jeanweaves_galleries.min.js'
    ]
    photos = []

    def get_page_context(self):
        page_context = super(JeanWeavesGalleryView, self).get_page_context()
        page_context['photos'] = self.photos
        return page_context


class JeanWeavesGalleryIndexView(JeanWeavesGalleryView):
    template_name = 'jeanweaves_galleries/index.html'
    photos = galleries.index


class JeanWeavesAnimalsGalleryView(JeanWeavesGalleryView):
    template_name = 'jeanweaves_galleries/animals.html'
    page_title = _('Animals')
    photos = galleries.animals


class JeanWeavesDamaskGalleryView(JeanWeavesGalleryView):
    template_name = 'jeanweaves_galleries/damask.html'
    page_title = _('Damask')
    photos = galleries.damask


class JeanWeavesPlacematsAndNapkinsGalleryView(JeanWeavesGalleryView):
    template_name = 'jeanweaves_galleries/placemats-and-napkins.html'
    page_title = _('Placemats and Napkins')
    photos = galleries.placemats_and_napkins


class JeanWeavesRunnersGalleryView(JeanWeavesGalleryView):
    template_name = 'jeanweaves_galleries/runners.html'
    page_title = _('Runners')
    photos = galleries.runners


class JeanWeavesScarvesGalleryView(JeanWeavesGalleryView):
    template_name = 'jeanweaves_galleries/scarves.html'
    page_title = _('Scarves')
    photos = galleries.scarves


class JeanWeavesThrowsGalleryView(JeanWeavesGalleryView):
    template_name = 'jeanweaves_galleries/throws.html'
    page_title = _('Throws')
    photos = galleries.throws


class JeanWeavesTowelsGalleryView(JeanWeavesGalleryView):
    template_name = 'jeanweaves_galleries/towels.html'
    page_title = _('Towels')
    photos = galleries.towels


THIRTY_DAYS = 60 * 60 * 24 * 30
index = cache_page(THIRTY_DAYS)(JeanWeavesGalleryIndexView.as_view())
animals = cache_page(THIRTY_DAYS)(JeanWeavesAnimalsGalleryView.as_view())
damask = cache_page(THIRTY_DAYS)(JeanWeavesDamaskGalleryView.as_view())
placemats_and_napkins = cache_page(THIRTY_DAYS)(JeanWeavesPlacematsAndNapkinsGalleryView.as_view())
runners = cache_page(THIRTY_DAYS)(JeanWeavesRunnersGalleryView.as_view())
scarves = cache_page(THIRTY_DAYS)(JeanWeavesScarvesGalleryView.as_view())
throws = cache_page(THIRTY_DAYS)(JeanWeavesThrowsGalleryView.as_view())
towels = cache_page(THIRTY_DAYS)(JeanWeavesTowelsGalleryView.as_view())
