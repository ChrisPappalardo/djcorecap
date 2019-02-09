# -*- coding: utf-8 -*-

'''
djcorecap/forms
---------------

form helpers and utilities
'''


from crispy_forms.layout import (
    Div,
    Field,
    Layout,
)


class FormRow(Layout):
    '''
    custom crispy layout for bootstrap form rows
    e.g. FormRow('field1', 'field2', ..., field_kwargs={...})
    '''

    row_kwargs = {'css_class': 'form-row'}
    col_kwargs = {}
    field_kwargs = {}

    def __init__(self, *fields, **kwargs):

        self.row_kwargs = kwargs.pop('row_kwargs', self.row_kwargs)
        self.col_kwargs = kwargs.pop('col_kwargs', self.col_kwargs)
        self.field_kwargs = kwargs.pop('field_kwargs', self.field_kwargs)

        super().__init__(
            Div(
                *[
                    Div(
                        Field(
                            field,
                            **self.field_kwargs,
                        ),
                        **self.col_kwargs,
                    ) for field in fields
                ],
                **self.row_kwargs,
            ),
            **kwargs,
        )
