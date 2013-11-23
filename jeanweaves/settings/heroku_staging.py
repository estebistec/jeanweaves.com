# -*- coding: utf-8 -*-
"Herkou staging deployment settings"


from .heroku_base import *


# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'jeanweaves.wsgi.heroku_staging.application'

ALLOWED_HOSTS = ['jeanweaves-staging.herokuapp.com']

GOOGLE_ANALYTICS_ID = 'UA-45942273-1'
GOOGLE_ANALYTICS_DOMAIN = 'jeanweaves-staging.herokuapp.com'
