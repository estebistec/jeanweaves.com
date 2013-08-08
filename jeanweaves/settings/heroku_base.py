# -*- coding: utf-8 -*-
"Heroku base deployment settings"


from .base import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = get_env_variable('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS += ('storages',)
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_ROOT = PROJECT_ROOT.child('collected_static')
STATIC_URL = 'https://s3.amazonaws.com/jeanweaves/'
AWS_ACCESS_KEY_ID = get_env_variable('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_env_variable('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'jeanweaves'

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

BLOG_BACKEND = 'jeanweaves_blog.blog.backends.tumblr'
TUMBLR_API_KEY = get_env_variable('TUMBLR_API_KEY')
TUMBLR_BLOG_NAME = u'jeanweaves'
