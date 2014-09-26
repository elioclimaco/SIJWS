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
def ListarExpedientes(request):
    """
    Lista los expedientes.
    """
    if request.method == 'GET':
        expedientes = expediente.objects.filter(n_ano_ingreso='2014', c_instancia='I05')
        serializer = ExpedienteSerializer(expedientes, many=True)
        return Response(serializer.data)