# -*- coding: utf-8 -*-


import urllib

from dateutil.parser import parse
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import requests
import pytz


TIME_ZONE = pytz.timezone(settings.TIME_ZONE)
WORDPRESS_POSTS_URI_TEMPLATE = 'https://public-api.wordpress.com/rest/v1/sites/{0}/posts/'


class Backend(object):

    def __init__(self):
        try:
            blog_name = settings.WORDPRESS_BLOG
        except AttributeError:
            raise ImproperlyConfigured(
                u'blog backend {} requires the WORDPRESS_BLOG setting'
                .format(__name__)
            )

        self.blog_posts_uri = u'{0}?{1}'.format(
            WORDPRESS_POSTS_URI_TEMPLATE.format(blog_name),
            urllib.urlencode({u'number': u'10', u'status': u'publish'})
        )

    def get_posts(self):
        response = requests.get(self.blog_posts_uri)
        response.raise_for_status()
        response_data = response.json()
        return [
            {
                u"date": parse(post[u"date"]).astimezone(TIME_ZONE),
                u"title": post[u"title"],
                u"content": post[u"content"]
            }
            for post in response_data[u'posts']
        ]
