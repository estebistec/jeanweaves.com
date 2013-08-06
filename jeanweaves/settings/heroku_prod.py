# -*- coding: utf-8 -*-
"Herkou prod deployment settings"


from .heroku_base import *


# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'jeanweaves.wsgi.heroku_prod.application'

ALLOWED_HOSTS = ['www.jeanweaves.com', 'jeanweaves.com']
