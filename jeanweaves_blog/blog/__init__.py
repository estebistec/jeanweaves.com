# -*- coding: utf-8 -*-


from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module


def get_backend_module_name():
	try:
		return settings.BLOG_BACKEND
	except AttributeError:
		raise ImproperlyConfigured(u'Missing required setting BLOG_BACKEND')


def load_backend_module():
    backend_module_name = get_backend_module_name()

    try:
        return import_module(backend_module_name)
    except ImportError as e:
        raise ImproperlyConfigured(
            'Error importing blog backend {}: {}'
            .format(backend_module_name, e)
        )


def load_backend():
    backend_module = load_backend_module()

    try:
    	Backend = backend_module.Backend
    except AttributeError:
    	raise ImproperlyConfigured(
    		'Blog backend {} does not define a Backend class'
    		.format(backend_module_name)
    	)

    return Backend()


blog = load_backend()
