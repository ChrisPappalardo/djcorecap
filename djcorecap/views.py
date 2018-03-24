# -*- coding: utf-8 -*-

'''
djcorecap/views
---------------

view mixins and other view helper utilities for django
'''

###############################################################################


from django.contrib import messages
from django.core.urlresolvers import reverse


def filter_by_user(model, user):
    '''
    helper function to filter queryset by user or all if superuser
    '''

    m = model.objects
    return m.all() if user.is_superuser else m.filter(user=user.id)


class SuccessUrlMixin(object):
    '''
    a mixin that generates `success_url` passing `success_url_args` from object
    '''

    @property
    def success_url(self):
        '''
        override this property with url name, standard with FormView, FormMixin
        '''

        return NotImplementedError

    @property
    def success_url_args(self):
        '''
        override this property with a sequence of attributes to pass from object
        '''

        return ()

    def get_success_url(self):
        '''
        constructs reverse call using `success_url` and `success_url_args`
        '''

        return reverse(
            self.success_url,
            kwargs={k: getattr(self.object, k) for k in self.success_url_args},
        )
