# -*- coding: utf-8 -*-


from dateutil.parser import parse
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import pytumblr

from jeanweaves_blog.blog.types import Post


class Backend(object):

	def __init__(self):
		try:
			self.blog_name = settings.TUMBLR_BLOG_NAME
		except AttributeError:
			raise ImproperlyConfigured(
				u'blog backend {} requires the TUMBLR_BLOG_NAME setting'
				.format(__name__)
			)

		try:
			tumblr_api_key = settings.TUMBLR_API_KEY
		except AttributeError:
			raise ImproperlyConfigured(
				u'blog backend {} requires the TUMBLR_API_KEY setting'
				.format(__name__)
			)

		self.tumblr = pytumblr.TumblrRestClient(tumblr_api_key)

	def get_posts(self):
		tumblr_posts = self.tumblr.posts(self.blog_name)
		return [
		    Post(
		    	title=post[u'title'],
		    	time=parse(post[u'date']),
		    	body=post[u'body']
		    )
		    for post in tumblr_posts[u'posts']
		    if post[u'state'] == u'published'
		]
