# -*- coding: utf-8 -*-


from dateutil.parser import parse
from django import template
from django.template.loader import render_to_string


register = template.Library()


@register.simple_tag
def tumblr_post(post):
	post[u'date'] = parse(post[u'date'])

	template_name = u'jeanweaves_blog/tumblr_posts/{}.html'.format(post['type'])
	return render_to_string(template_name, {u'post': post})
