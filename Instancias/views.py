from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *

class DistritoArbol(viewsets.ModelViewSet):
    queryset = distrito_judicial.objects.all()
    serializer_class = DistritoSerializer

class SedeArbol(viewsets.ModelViewSet):
    queryset = sede.objects.all()
    serializer_class = SedeSerializer

class JuzgadoArbol(viewsets.ModelViewSet):
    queryset = instancia.objects.all()
    serializer_class = JuzgadoSerializer