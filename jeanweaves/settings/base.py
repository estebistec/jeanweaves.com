# -*- coding: utf-8 -*-
# Django settings for jeanweaves project.


import os

from django.core.exceptions import ImproperlyConfigured
from unipath import Path

import jeanweaves.jinja_safestrings


def get_env_variable(var_name):
    """Get the named environment variable or raise ImproperlyConfigured"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Missing the {} env variable".format(var_name)
        raise ImproperlyConfigured(error_msg)


PROJECT_ROOT = Path(__file__).ancestor(3)

ADMINS = (
    ('Steven Cummings', 'jeanweavesdev@gmail.com'),
)

MANAGERS = ADMINS


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # django.conf.global_settings.TEMPLATE_CONTEXT_PROCESSORS:
    # "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    # "django.contrib.messages.context_processors.messages",

    'jeanweaves_public.context_processors.site_info',
    # 'jeanweaves_public.context_processors.analytics',
    'jeanweaves_galleries.context_processors.galleries',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'jeanweaves.urls'

INSTALLED_APPS = (
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',

    'django.contrib.staticfiles',

    # 'django.contrib.admin',
    # 'django.contrib.admindocs',

    'coffin',

    'jeanweaves_public',
    'jeanweaves_galleries',
    'jeanweaves_blog',
)
