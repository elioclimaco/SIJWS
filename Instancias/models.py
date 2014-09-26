from django.db import models

class distrito_judicial(models.Model):
    c_distrito = models.CharField(primary_key=True, max_length=3)
    c_jurisprudencia = models.CharField(max_length=4)
    c_ubigeo = models.CharField(max_length=10)
    COD_ORG_DEP_SIS = models.IntegerField()
    IDOFIORGCODIGO = models.CharField(max_length=2)
    latitud_dist = models.CharField(max_length=20)
    longitud_dist = models.CharField(max_length=20)
    x_nom_distrito = models.CharField(max_length=30)

    def __unicode__(self):
        return self.x_nom_distrito

    class Meta:
        db_table = 'distrito_judicial'


class sede(models.Model):
    c_sede = models.CharField(primary_key=True, max_length=4, db_column='c_sede')
    c_codigo_app = models.CharField(max_length=2)
    c_distrito = models.CharField(max_length=3)
    c_sede_corte = models.CharField(max_length=4)
    c_sede_prin = models.CharField(max_length=4)
    l_activo = models.CharField(max_length=1)
    l_produccion = models.CharField(max_length=1)
    latitud_sede = models.CharField(max_length=20)
    longitud_sede = models.CharField(max_length=20)
    x_desc_sede = models.CharField(max_length=60)
    x_direccion = models.CharField(max_length=150)

    def __unicode__(self):
        return self.x_desc_sede

    class Meta:
        db_table = 'sede'


class instancia(models.Model):
    #c_distrito = models.ForeignKey(distrito_judicial, related_name='distrito')
    #c_instancia = models.CharField(max_length=3)
    c_instancia = models.CharField(primary_key=True)
    c_org_jurisd = models.CharField(max_length=2)
    c_org_jurisd_suprema = models.CharField(max_length=2)
    c_provincia = models.CharField(max_length=4)
    c_sede = models.ForeignKey(sede, related_name='Sede', db_column='c_sede')
    c_ubigeo = models.CharField(max_length=10)
    cod_unico_instancia = models.CharField(max_length=6)
    contador_ing = models.IntegerField()
    dns_db_id = models.IntegerField()
    eq_codg_archivo = models.CharField(max_length=6)
    eq_codg_central = models.CharField(max_length=6)
    l_asig = models.CharField(max_length=1)
    l_carcel = models.CharField(max_length=1)
    l_ind_baja = models.CharField(max_length=1)
    l_ind_barcode = models.CharField(max_length=1)
    l_ind_bd = models.CharField(max_length=1)
    l_ind_cms = models.CharField(max_length=1)
    l_ind_electronico = models.CharField(max_length=1)
    l_ind_ingreso = models.IntegerField()
    l_ind_ped = models.IntegerField()
    l_ind_turno = models.CharField(max_length=1)
    l_independiente = models.CharField(max_length=1)
    l_modulo_ejecucion = models.CharField(max_length=1)
    l_munica = models.CharField(max_length=1)
    l_par_impar = models.CharField(max_length=1)
    l_servidor_atachado = models.CharField(max_length=1)
    l_sij = models.CharField(max_length=1)
    n_carga_envio = models.IntegerField()
    n_carga_guia_tp = models.IntegerField()
    n_carga_max = models.IntegerField()
    n_carga_procesal = models.IntegerField()
    n_carga_proceso_eleva = models.IntegerField()
    n_carga_redistribucion = models.IntegerField()
    n_dependencia = models.IntegerField()
    n_distrito = models.IntegerField()
    n_escenario = models.IntegerField()
    n_instancia = models.IntegerField()
    n_instancia_id = models.IntegerField()
    n_juzgado = models.IntegerField()
    n_maximo = models.IntegerField()
    n_modulo = models.IntegerField()
    provincia = models.IntegerField()
    x_corto = models.CharField(max_length=4)
    x_nom_instancia = models.CharField(max_length=60)
    x_ubicacion_fisica = models.CharField(max_length=50)

    class Meta:
            db_table = 'instancia'
            # unique_together = (('c_distrito', 'c_instancia', 'c_provincia'),)
            #unique_together = (('c_distrito', 'c_instancia'),)

    def __unicode__(self):
        return '%s %s' %(self.c_instancia, self.x_nom_instancia)




    #
    # c_distrito = models.ForeignKey(distrito_judicial, related_name='distrito')
    # c_instancia = models.CharField(max_length=3)
    # c_org_jurisd = models.CharField(max_length=2)
    # c_org_jurisd_suprema = models.CharField(max_length=2)
    # c_provincia = models.CharField(max_length=4)
    # c_sede = models.ForeignKey(sede, related_name='sede')
    # c_ubigeo = models.CharField(max_length=10)
    # cod_unico_instancia = models.CharField(max_length=6)
    # contador_ing = models.IntegerField()
    # dns_db_id = models.IntegerField()
    # eq_codg_archivo = models.CharField(max_length=6)
    # eq_codg_central = models.CharField(max_length=6)
    # l_asig = models.CharField(max_length=1)
    # l_carcel = models.CharField(max_length=1)
    # l_ind_baja = models.CharField(max_length=1)
    # l_ind_barcode = models.CharField(max_length=1)
    # l_ind_bd = models.CharField(max_length=1)
    # l_ind_cms = models.CharField(max_length=1)
    # l_ind_electronico = models.CharField(max_length=1)
    # l_ind_ingreso = models.IntegerField()
    # l_ind_ped = models.IntegerField()
    # l_ind_turno = models.CharField(max_length=1)
    # l_independiente = models.CharField(max_length=1)
    # l_modulo_ejecucion = models.CharField(max_length=1)
    # l_munica = models.CharField(max_length=1)
    # l_par_impar = models.CharField(max_length=1)
    # l_servidor_atachado = models.CharField(max_length=1)
    # l_sij = models.CharField(max_length=1)
    # n_carga_envio = models.IntegerField()
    # n_carga_guia_tp = models.IntegerField()
    # n_carga_max = models.IntegerField()
    # n_carga_procesal = models.IntegerField()
    # n_carga_proceso_eleva = models.IntegerField()
    # n_carga_redistribucion = models.IntegerField()
    # n_dependencia = models.IntegerField()
    # n_distrito = models.IntegerField()
    # n_escenario = models.IntegerField()
    # n_instancia = models.IntegerField()
    # n_instancia_id = models.IntegerField()
    # n_juzgado = models.IntegerField()
    # n_maximo = models.IntegerField()
    # n_modulo = models.IntegerField()
    # provincia = models.IntegerField()
    # x_corto = models.CharField(max_length=4)
    # x_nom_instancia = models.CharField(max_length=60)
    # x_ubicacion_fisica = models.CharField(max_length=50)

