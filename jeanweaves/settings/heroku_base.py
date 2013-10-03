# -*- coding: utf-8 -*-
"Heroku base deployment settings"


from .base import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'root': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

BLOG_BACKEND = 'jeanweaves_blog.blog.backends.wordpress'
WORDPRESS_BLOG = 'jeanweaves.wordpress.com'
