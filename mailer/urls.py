#-*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.urls import path
from . import views

# from mailer.views import IndexView

urlpatterns = [
    # url(r'^$', IndexView.as_view(), name="index"),
    path('', views.index, name='index'),
]
