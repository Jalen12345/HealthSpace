#
# urls.py
# group25django
# 
# Created by Jeffrey Wang on 19/10/2021.
# Copyright © 2021 ecalrsoft.io. All rights reserved.
#

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('^$', views.home),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('diet/', views.diet, name='diet'),
    path('exercise/', views.exercise, name='exercise'),
    path('form/', views.form, name='form'),
    path('login/', views.login, name='login'),
    path('sleep/', views.sleep, name='sleep')
]