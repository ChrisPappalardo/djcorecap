# -*- coding: utf-8 -*-

'''
djcorecap/templatetags/core
---------------------------

core templatetags for the djcorecap app
'''

import re

from django import template
from django.urls import reverse, NoReverseMatch


register = template.Library()


@register.simple_tag(takes_context=True)
def active_url(context, url):
    '''
    returns 'active' if url matches request.path in context
    '''

    path = context['request'].path

    try:

        # if url reverses, use that as the pattern (e.g. '/foo/')
        pattern = '^%s$' % reverse(url)

    except NoReverseMatch as e:

        # otherwise use url as the pattern
        pattern = url

    return 'active' if re.search(pattern, path) else ''
