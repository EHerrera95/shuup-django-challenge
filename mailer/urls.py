#-*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.urls import path
from . import views

#from mailer.views import IndexView

# I just prefer to use request view to add more context to pass to template rather than class-based View
# from the resources and studies I read, there is no real difference in speed and efficiency between the two

urlpatterns = [
    #url(r'^$', IndexView.as_view(), name="index"),
    path('', views.index, name='index'),
]
