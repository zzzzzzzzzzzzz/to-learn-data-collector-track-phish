# -*- coding: utf-8 -*-

from django import forms
from django.forms import Textarea


class UrlInputForm(forms.Form):
    urls = forms.CharField(widget=forms.Textarea)

