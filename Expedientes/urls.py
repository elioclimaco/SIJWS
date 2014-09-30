# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = patterns('',
    #url(r'^prueba/$', Expedientes, name='Prueba'),

    #url(r'^listar/$', ListarExpedientes, name='ExpedientesListar'),

    # Lista expedientes por Distrito y Juzgado.
    # http://localhost/juzgado/1/expedientes
    url(r'^distrito/(?P<distrito>\w+)/juzgado/(?P<juzgado>\w+)/$', ExpedientesPorJuzgado, name='ExpedientesPorJuzgado'),
    #url(r'^sede/(?P<sede>\d+)/instancias/$', Instancias, name = 'Instancias'),



)

urlpatterns = format_suffix_patterns(urlpatterns)