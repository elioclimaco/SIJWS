# -*- coding: utf-8 -*-
from django.db import models

#
# Accediendo a las Vistas creadas en la base de datos
#
class vw_expediente(models.Model):
    id = models.IntegerField(primary_key=True, db_column='nid_unico')
    #nid_unico = models.IntegerField(primary_key=True, db_column='nid_unico')
    nid_unico = models.IntegerField()
    nid_incidente = models.IntegerField()
    txt_especialidad = models.CharField(max_length=30)
    cod_expediente = models.CharField(max_length=33)
    cod_distrito = models.CharField(max_length=3)
    cod_instancia = models.CharField(max_length=3)
    txt_instancia = models.CharField(max_length=60)
    txt_distrito = models.CharField(max_length=30)
    txt_juez = models.CharField(max_length=13)
    txt_especialista = models.CharField(max_length=50)
    txt_procedencia = models.CharField(max_length=70)
    txt_proceso = models.CharField(max_length=30)
    txt_observacion = models.CharField(max_length=200)
    txt_materia = models.CharField(max_length=150)
    cod_estado = models.CharField(max_length=3)
    cod_etapa = models.CharField(max_length=1)
    txt_estado = models.CharField(max_length=60)
    txt_etapa = models.CharField(max_length=7)
    txt_ubicacion = models.CharField(max_length=90)
    cod_conclusion = models.CharField(max_length=3)
    txt_conclusion = models.CharField(max_length=200)
    cod_visualiza = models.CharField(max_length=1)
    txt_sumilla = models.CharField(max_length=600)
    txt_partes = models.CharField(max_length=1)
    fec_inicio = models.DateTimeField()
    fec_conclusion = models.DateTimeField()
    cod_medida_cautelar = models.CharField(max_length=6)
    c_org_jurisd = models.CharField(max_length=2)
    f_ingreso = models.DateTimeField()

    def __unicode__(self):
        return self.cod_expediente

    class Meta:
        managed = False
        db_table = 'websj\".\"vw_expediente'
