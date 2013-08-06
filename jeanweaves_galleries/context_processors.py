# -*- coding: utf-8 -*-


def galleries(request):
    return {
        'galleries': {
            'base_layout': 'jeanweaves_public/_layout.html',
            'base_photo_url': 'https://s3.amazonaws.com/jeanweaves.com/'  # TODO static root?
        }
    }
