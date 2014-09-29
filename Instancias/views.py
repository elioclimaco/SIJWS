from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *

class DistritoArbol(viewsets.ModelViewSet):
    queryset = distrito_judicial.objects.filter(c_distrito=29)
    serializer_class = DistritoSerializer

class SedeArbol(viewsets.ModelViewSet):
    queryset = sede.objects.filter(c_sede=2903)
    serializer_class = SedeSerializer

class JuzgadoArbol(viewsets.ModelViewSet):
    queryset = instancia.objects.all()
    serializer_class = JuzgadoSerializer