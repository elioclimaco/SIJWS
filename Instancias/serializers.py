# -*- coding: utf-8 -*-
__author__ = 'Elio Clímaco'

from rest_framework import serializers

from .models import *



#
# Órganos Jurisdiccionales
#
class JuzgadoSerializer(serializers.ModelSerializer):
    id = serializers.Field(source='c_instancia')
    text = serializers.Field(source='x_nom_instancia')
    class Meta:
        model = instancia
        fields = ('id', 'text')


class SedeSerializer(serializers.ModelSerializer):
    id = serializers.Field(source='c_sede')
    text = serializers.Field(source='x_desc_sede')
    children = JuzgadoSerializer(many=True, source='sede')
    class Meta:
        model = sede
        fields = ('id', 'text', 'children')
        #fields = ('id', 'text')


class DistritoSerializer(serializers.ModelSerializer):
    id = serializers.Field(source='c_distrito')
    text = serializers.Field(source='x_nom_distrito')
    children = SedeSerializer(many=True, source='distrito')
    class Meta:
        model = distrito_judicial
        fields = ('id', 'text', 'children')
        #fields = ('id', 'text')