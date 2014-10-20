# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = patterns('',
    #url(r'^prueba/$', Expedientes, name='Prueba'),

    # Lista expedientes por Distrito y Juzgado.
    url(r'^distrito/(?P<distrito>\w+)/juzgado/(?P<juzgado>\w+)/$', ExpedientesPorJuzgado, name='ExpedientesPorJuzgado'),
)

urlpatterns = format_suffix_patterns(urlpatterns)