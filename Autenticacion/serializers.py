# -*- coding: utf-8 -*-
__author__ = 'Elio Clímaco'

from rest_framework import serializers
from .models import *

class UsuariosSerializer(serializers.ModelSerializer):
    Usuario = serializers.Field(source='c_usuario')
    TipoUsuario = serializers.Field(source='l_tipo_usuario')
    Nombre = serializers.Field(source='x_nom_usuario')
    Expediente = serializers.Field(source='n_nro_exp')
    Equipo = serializers.Field(source='c_equipo')
    Estado = serializers.Field(source='l_conectado')
    Clave = serializers.Field(source='c_clave')
    Fotocheck = serializers.Field(source='c_foto_check')
    Perfil = serializers.Field(source='c_perfil')
    Temporizador = serializers.Field(source='n_temporizador')
    CambioClave = serializers.Field(source='fec_cambio_clave')
    DiasClave = serializers.Field(source='num_dias_clave')
    ClaveVocal = serializers.Field(source='c_clave_vocal')
    TipoRedistribucion = serializers.Field(source='l_tipo_redist')
    Distrito = serializers.Field(source='c_distrito')
    Provincia = serializers.Field(source='c_provincia')
    Sede = serializers.Field(source='c_sede')
    Activo = serializers.Field(source='l_activo')
    RecibeCarga = serializers.Field(source='l_recibe_carga')
    Imprime = serializers.Field(source='l_ind_print')
    FechaAuditoria = serializers.Field(source='f_aud')
    Auditoria = serializers.Field(source='b_aud')
    Auditor = serializers.Field(source='c_aud_uid')
    PCUsuario = serializers.Field(source='c_aud_uidred')
    PCNombre = serializers.Field(source='c_aud_pc')
    PCIP = serializers.Field(source='n_aud_ip')
    PCMac = serializers.Field(source='c_aud_mcaddr')
    CargaProcesal = serializers.Field(source='n_carga_procesal')
    Grupo = serializers.Field(source='n_grupo')
    Antiguedad = serializers.Field(source='l_antiguedad')
    UltimoAsignado = serializers.Field(source='l_ultimo_asig')
    UsuarioGRJ = serializers.Field(source='l_usuario_grj')
    DNI = serializers.Field(source='c_dni')
    ApellidoPaterno = serializers.Field(source='c_ape_paterno')
    ApellidoMaterno = serializers.Field(source='c_ape_materno')
    Nombres = serializers.Field(source='c_nombres')
    FechaNacimiento = serializers.Field(source='f_nac')
    ValidoRENIEC = serializers.Field(source='c_flag_valid_reniec')
    Correo = serializers.Field(source='l_correo')
    DescCorreo = serializers.Field(source='x_desc_correo')
    SIJRENIEC = serializers.Field(source='l_sij_reniec')
    RegistroRENIEC = serializers.Field(source='f_reg_reniec')
    OficRENIEC = serializers.Field(source='l_ofic_reniec')
    ClaveDJE = serializers.Field(source='c_clave_dje')
    LogeadoSIJ = serializers.Field(source='l_logeado_sij')
    SesionMultiple = serializers.Field(source='l_sesion_multiple')
    IPLogeo = serializers.Field(source='x_ip_address_log')
    MacLogeo = serializers.Field(source='x_mc_address_log')
    PCNombreLogeo = serializers.Field(source='x_usuario_red_log')

    class Meta:
        model = usuario
        fields = (u'Usuario', u'Nombre', 'Clave', 'ClaveDJE')