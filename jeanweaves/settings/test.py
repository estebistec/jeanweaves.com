# -*- coding: utf-8 -*-
"test execution settings"


from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG


EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'null': {
            'level': 'CRITICAL',
            'class': 'django.utils.log.NullHandler',
        },
    },
    'loggers': {
        'root': {
            'handlers': ['null'],
            'level': 'CRITICAL',
            'propagate': False,
        },
    }
}
