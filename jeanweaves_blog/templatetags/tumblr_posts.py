# -*- coding: utf-8 -*-


from dateutil.parser import parse
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django_jinja import library
import pytz


TIME_ZONE = pytz.timezone(settings.TIME_ZONE)

lib = library.Library()


@lib.global_function
def render_tumblr_post(post):
    # NOTE doing astimezone since coffin doesn't seem to have jinja implement
    # Django l10n features
    post[u'date'] = parse(post[u'date']).astimezone(TIME_ZONE)

    template_name = u'jeanweaves_blog/tumblr_posts/{}.html'.format(post['type'])
    try:
        rendered_post = render_to_string(template_name, {u'post': post})
        return mark_safe(rendered_post)
    except Exception as e:
        print str(e)
        return ''
