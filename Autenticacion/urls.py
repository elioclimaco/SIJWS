# -*- coding: utf-8 -*-
__author__ = 'Elio Clímaco'

from django.conf.urls import url, patterns
from .views import *


urlpatterns = patterns('',
   url(r'^distrito/(?P<distrito>\d+)/$', UsuariosListar, name='Usuarios'),
)
