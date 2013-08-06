# -*- coding: utf-8 -*-


def site_info(request):
    return {
        'site': {
            'title': 'Jean Williams, Handweaver',  # TODO i18n
            'author': 'Jean Williams',
            'author_email': 'jeanweaves@gmail.com',
            'description': 'Jean Williams, Handweaver',  # TODO i18n
            'copyright': "2013"  # TODO dynamic and cached
        }
    }


def analytics(request):
    return {
        'analytics': {
            'google_analytics_id': ''  # TODO UA-XXXXX-X
        }
    }
