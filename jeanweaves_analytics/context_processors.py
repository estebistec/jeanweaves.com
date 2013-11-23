# -*- coding: utf-8 -*-


from django.conf import settings


def analytics(request):
    return {
        'analytics': {
            'google_analytics_id': getattr(settings, 'GOOGLE_ANALYTICS_ID', None),
            'google_analytics_domain': getattr(settings, 'GOOGLE_ANALYTICS_DOMAIN', 'auto'),
        }
    }
