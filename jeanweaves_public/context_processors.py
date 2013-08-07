# -*- coding: utf-8 -*-


from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


def site_info(request):
    return {
        'site': {
            'title': 'Jean Williams, Handweaver',  # TODO i18n
            'author': 'Jean Williams',
            'author_email': 'jeanweaves@gmail.com',
            'description': 'Jean Williams, Handweaver',  # TODO i18n
            'copyright': '2013',  # TODO dynamic and cached
            'nav': [
                {'href': reverse('index'), 'title': _('Home'), 'label': _('Home')},
                {'href': reverse('about'), 'title': _('About'), 'label': _('About')},
                {'href': reverse('exhibits'), 'title': _('Exhibits'), 'label': _('Exhibits')},
                #{'href': reverse('tools'), 'title': _('Tools'), 'label': _('Tools')},
                {'href': reverse('contact'), 'title': _('Contact me'), 'label': _('Contact me')},
            ],
        }
    }


def analytics(request):
    return {
        'analytics': {
            'google_analytics_id': ''  # TODO UA-XXXXX-X
        }
    }
