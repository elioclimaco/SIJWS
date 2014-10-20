# -*- coding: utf-8 -*-
__author__ = 'Elio Clímaco'

from django.conf.urls import patterns, url
from .views import *

urlpattern = patterns('',
    url(r'^juzgados/$', JuzgadoArbol, name='JuzgadoArbol'),

)


