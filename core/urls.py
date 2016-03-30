# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^login/', login, {'template_name': 'core/login.html'}, name="login"),
    url(r'^logout/', logout, {'next_page': 'index'}, name="logout")
]