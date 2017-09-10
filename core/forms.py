# -*- coding: utf-8 -*-

from django import forms


class UrlInputForm(forms.Form):
    urls = forms.CharField()
