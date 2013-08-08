# -*- coding: utf-8 -*-


from dateutil.parser import parse

from jeanweaves_blog.blog.types import Post


class Backend(object):

  def get_posts(self):
    return [
        Post(
          title=u'Test',
          time=parse(u'2013-08-07 01:27:10 GMT'),
          body=u'<p>Test</p>'
        ),
        Post(
          title=u'List test',
          time=parse(u'2013-08-06 01:27:10 GMT'),
          body=u'<ul><li>A</li><li>B</li><li>C</li></ul>'
        ),
        Post(
          title=u'Test',
          time=parse(u'2013-08-05 01:27:10 GMT'),
          body=u'<p>Test</p>'
        )
    ]
