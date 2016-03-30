# -*- coding: utf-8 -*-

from django import forms


class QuestionListForm(forms.Form):

    search = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(('id', 'ID'), ('created_at', u'Дата создания')), required=False)

