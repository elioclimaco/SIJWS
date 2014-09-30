from django.shortcuts import render
from django.views.generic import TemplateView, ListView


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .serializers import *
from .vistasBD import *
from .models import *



@api_view(['GET'])
def ExpedientesPorJuzgado(request, distrito, juzgado):
    """
    Lista los expedientes por Distrito e Instancia Judicial, desde la
    vista vw_expediente de la base de datos.
    """
    if request.method == 'GET':
        expedientes = vw_expediente.objects.filter(cod_distrito=distrito, cod_instancia=juzgado)
        serializer = ExpedienteSerializer(expedientes, many=True)
        return Response(serializer.data)