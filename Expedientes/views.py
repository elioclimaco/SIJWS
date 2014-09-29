from django.shortcuts import render
from django.views.generic import TemplateView, ListView


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .serializers import *
from .models import *


class Prueba(ListView):
    model = expediente
    template_name = 'expedientes/prueba.html'


class ExpedientesListar(generics.ListAPIView):
    queryset = expediente.objects.filter(n_ano_ingreso='2014', c_instancia='I05')
    serializer_class = ExpedienteSerializer


@api_view(['GET'])
def ExpedientesPorJuzgado(request, distrito, juzgado):
    """
    Lista los expedientes, por Distrito Judicial, Instancia Judicial, Anulado .
    """
    if request.method == 'GET':
        expedientes = expediente.objects.filter(c_distrito=distrito, c_instancia=juzgado, l_anulado='S')
        serializer = ExpedienteSerializer(expedientes, many=True)
        return Response(serializer.data)