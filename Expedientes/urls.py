# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = patterns('',
    url(r'^prueba/$', Prueba.as_view(), name='Prueba'),

    url(r'^listar/$', ListarExpedientes, name='ExpedientesListar'),
)

urlpatterns = format_suffix_patterns(urlpatterns)