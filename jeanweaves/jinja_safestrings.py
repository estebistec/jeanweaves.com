# -*- coding: utf-8 -*-
'''Monkeypatch Django to mimic Jinja2 behaviour.

See: https://github.com/coffin/coffin#autoescape'''


from django.utils import safestring


if not hasattr(safestring, '__html__'):
    safestring.SafeString.__html__ = lambda self: str(self)
    safestring.SafeUnicode.__html__ = lambda self: unicode(self)
