# -*- coding: utf-8 -*-
__author__ = 'Elio Clímaco'

from rest_framework import serializers

from .models import *
from .vistasBD import *

# class ExpedienteSerializer(serializers.ModelSerializer):
#     expediente = serializers.Field(source='x_formato')
#     sumilla = serializers.Field(source='x_sumilla')
#     class Meta:
#         model = expediente
#         fields = ('expediente', 'sumilla', 'n_nro_exp_origen')

class ExpedienteSerializer(serializers.ModelSerializer):
    expediente = serializers.Field(source='cod_expediente')

    id = serializers.Field(source='nid_unico')
    Expediente = serializers.Field(source='cod_expediente')
    Incidente = serializers.Field(source='nid_incidente')
    Especialidad = serializers.Field(source='txt_especialidad')
    Sumilla = serializers.Field(source='txt_sumilla')
    codDistrito = serializers.Field(source='cod_distrito')
    Distrito = serializers.Field(source='txt_distrito')
    codInstancia = serializers.Field(source='cod_instancia')
    Instancia = serializers.Field(source='txt_instancia')
    Juez = serializers.Field(source='txt_juez')
    Especialista = serializers.Field(source='txt_especialista')
    Procedencia = serializers.Field(source='txt_procedencia')
    Proceso = serializers.Field(source='txt_proceso')
    Observacion = serializers.Field(source='txt_observacion')
    Materia = serializers.Field(source='txt_materia')
    codEstado = serializers.Field(source='cod_estado')
    Estado = serializers.Field(source='txt_estado')
    codEtapa = serializers.Field(source='cod_etapa')
    Etapa = serializers.Field(source='txt_etapa')
    Ubicacion = serializers.Field(source='txt_ubicacion')
    codConclusion = serializers.Field(source='cod_conclusion')
    Conclusion = serializers.Field(source='txt_conclusion')
    codVisualiza = serializers.Field(source='cod_visualiza')
    Partes = serializers.Field(source='txt_partes')
    FechaInicio = serializers.Field(source='fec_inicio')
    FechaConclusion = serializers.Field(source='fec_conclusion')
    MedidaCautelar = serializers.Field(source='cod_medida_cautelar')
    Organo = serializers.Field(source='c_org_jurisd')
    FechaRegistro = serializers.Field(source='f_ingreso')

    class Meta:
        model = vw_expediente
        fields = (  'id', 'Expediente', 'Incidente', 'Especialidad',
                    'Sumilla', 'codDistrito', 'Distrito', 'codInstancia',
                    'Instancia', 'Juez', 'Especialista', 'Procedencia',
                    'Proceso', 'Observacion', 'Materia', 'codEstado',
                    'Estado', 'codEtapa', 'Etapa', 'Ubicacion',
                    'codConclusion', 'Conclusion', 'codVisualiza', 'Partes',
                    'FechaInicio', 'FechaConclusion', 'MedidaCautelar', 'Organo',
                    'FechaRegistro'
        )
