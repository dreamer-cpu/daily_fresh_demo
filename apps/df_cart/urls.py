#!/user/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'df_cart'

urlpatterns = [
    url(r'^$', views.cart),
    url(r'^add(\d+)_(\d+)/$', views.add),
    url(r'^edit(\d+)_(\d+)/$', views.edit),
    url(r'^delete(\d+)/$', views.delete),
]
