# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from Instancias.views import *

router = routers.DefaultRouter()
router.register(r'Juzgado', JuzgadoArbol)
router.register(r'Sede', SedeArbol)
router.register(r'Distrito', DistritoArbol)

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SIJWS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Enlazando la API para el ruteo automático de las URL's
    url(r'^', include(router.urls)),

    # Incluyendo las URL's para la API navegable
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),

    # Expedientes
    url(r'^expedientes/', include('Expedientes.urls', namespace='Expedientes')),

    # Instancias
    url(r'^instancias/', include('Instancias.urls', namespace='Instancias')),
)
