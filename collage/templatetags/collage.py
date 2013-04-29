# -*- coding: utf-8 -*-

from django.conf import settings
from django import template

from bricks import Collage


class GetCollage(template.Node):
    def __init__(self, bits):
        self.bits = bits

    def _debug(self):
        return Collage().run(template.resolve_variable(
            self.bits[2], self.context))

    def _disable_exceptions(self):
        try:
            return self._debug()
        except:
            pass

    def set_context(self, results):
        self.context[self.bits[4]] = results
        return ''

    def render(self, context):
        self.context = context
        if settings.TEMPLATE_DEBUG:
            return self.set_context(self._debug())
        return self.set_context(self._disable_exceptions())


def get_collage(parser, token):
    return GetCollage(token.contents.split())


register = template.Library()
register.tag(get_collage)
