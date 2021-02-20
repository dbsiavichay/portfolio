# blog/templatetags/markdownify.py
from django import template
from django.template.defaultfilters import stringfilter

import markdown as md
from markdown.extensions.codehilite import CodeHiliteExtension

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code', CodeHiliteExtension(css_class='highlight')])
