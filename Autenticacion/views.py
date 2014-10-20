# -*- coding: utf-8 -*-
__author__ = 'Elio Clímaco'

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *

@api_view(['GET'])
def UsuariosListar(request, distrito):
    """
    Lista los usuarios por Distrito.
    """
    if request.method == 'GET':
        usuarios = usuario.objects.filter(c_distrito=distrito)
        serializer = UsuariosSerializer(usuarios, many=True)
        return Response(serializer.data)