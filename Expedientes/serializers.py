# -*- coding: utf-8 -*-
__author__ = 'Elio Clímaco'

from rest_framework import serializers

from .models import *

class ExpedienteSerializer(serializers.ModelSerializer):
    expediente = serializers.Field(source='x_formato')
    sumilla = serializers.Field(source='x_sumilla')
    class Meta:
        model = expediente
        fields = ('expediente', 'sumilla', 'n_nro_exp_origen')



