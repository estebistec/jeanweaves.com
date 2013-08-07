# -*- coding: utf-8 -*-


from django.conf import settings


def galleries(request):
    return {
        'galleries': {
            'base_layout': 'jeanweaves_public/_layout.html',
            'base_photo_url': settings.STATIC_URL
        }
    }
