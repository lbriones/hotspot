# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models
from geoposition.fields import GeopositionField
from datetime import datetime    
#from tinymce import models as tinymce_models

##plugins googlemaps locations
    

class Cliente(models.Model):
    cliente = models.CharField(max_length=45, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True, unique=True) 
    rut = models.CharField(max_length=12, blank=True, null=True, unique=True)
    logo = models.ImageField(upload_to='images/logos_clientes', help_text='50x50px image')
    created = models.DateTimeField(default=datetime.now, blank=True)
    Activo = models.BooleanField(default=True)
    #def image_tag(self):
    #    return u'<img src="%s" />' % MEDIA_URL + self.logo.url
    #image_tag.short_description = 'Image'
    #image_tag.allow_tags = True

    def __unicode__(self):
        return unicode(self.cliente)

class Campana(models.Model):
    cliente = models.ForeignKey(Cliente)
    nombre_campana = models.CharField(max_length=150, blank=True, null=True)
    titulo = models.CharField(max_length=150, blank=True, null=True)
    #body = tinymce_models.HTMLField()
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(default=datetime.now, blank=True)
    Activo = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.campana)


class Zona(models.Model):
    nombre = models.CharField(max_length=255, default='sin asignar')
    created = models.DateTimeField(default=datetime.now, blank=True)
    Activo = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.nombre)

class Router(models.Model):
    router_key = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=255, default='sin asignar')
    mac = models.CharField(max_length=20, blank=True, null=True)
    zona = models.ForeignKey(Zona, blank=True, null=True)
    position = GeopositionField()
    location = models.CharField(max_length=255, default='sin asignar')
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    updatedmac = models.CharField(max_length=20, blank=True, null=True)  # Field name made lowercase.
    updatedip = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    updatedproxyip = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    metadata = models.CharField(max_length=255, blank=True, null=True)
    
    def __unicode__(self):
        return unicode(self.name)

class RedWifi(models.Model):
    ssid_key = models.CharField(max_length=32, primary_key=True)
    router = models.ForeignKey(Router)
    name = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(max_length=20, blank=True, null=True)  # Field name made lowercase.
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    nas = models.IntegerField(blank=True, null=True)
    updatedmac = models.CharField(max_length=20, blank=True, null=True)  # Field name made lowercase.
    updatedip = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    updatedproxyip = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    landing = models.URLField()
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    metadata = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)

class Usuario(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True, unique=True) 
    password = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    sexo = models.IntegerField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    email_notificacion = models.IntegerField(blank=True, null=True)
    rut = models.CharField(max_length=10, blank=True, null=True)
    msg_total = models.IntegerField(blank=True, null=True)
    msg_send = models.IntegerField(blank=True, null=True)
    sms_code = models.CharField(max_length=5, blank=True, null=True)
    created = models.DateTimeField(default=datetime.now, blank=True)
    Activo = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.email)

class Sesion(models.Model):
    mac = models.CharField(max_length=25, blank=True, null=True)
    rssi = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    tiempo_conexion = models.IntegerField(blank=True, null=True)
    current = models.IntegerField(blank=True, null=True)
    redwifi = models.ForeignKey(RedWifi, blank=True, null=True)
    
    def __unicode__(self):
        return unicode(self.mac)


class Telefono(models.Model):
    mac = models.CharField(max_length=45, blank=True, null=True)
    so = models.CharField(max_length=20, blank=True, null=True)
    device = models.CharField(max_length=100, blank=True, null=True)
    push = models.CharField(max_length=250, blank=True, null=True)
    useragent = models.CharField(max_length=250, blank=True, null=True)
    sdk = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(default=datetime.now, blank=True)


class Campo(models.Model):
    campo = models.CharField(max_length=256)
    language = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s (%s)" % (force_unicode(self.campo), force_unicode(self.language))


class Local(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="ascii name")
    alt_names = models.ManyToManyField('Campos')

    class Meta:
        abstract = True

    @property
    def hierarchy(self):
        """Get hierarchy, root first"""
        list = self.parent.hierarchy if self.parent else []
        list.append(self)
        return list

    def get_absolute_url(self):
        return "/".join([local.slug for local in self.hierarchy])

    def __unicode__(self):
        return force_unicode(self.name)


"""
class IconoCampana(models.Model):
    cliente = models.ForeignKey(Cliente)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.nombre)

class Plantilla(models.Model):
    nombre = models.CharField(max_length=150, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.nombre)

class CampoPlantilla(models.Model):
    plantilla = models.ForeignKey(Plantilla)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.nombre)

class ImagenCampana(models.Model):
    cliente = models.ForeignKey(Cliente)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)

class FiltroEtiqueta(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    operador_valido = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

class Campana(models.Model):
    cliente = models.ForeignKey(Cliente)
    plantilla = models.ForeignKey(Plantilla)
    icono_campana = models.ForeignKey(IconoCampana)
    campana = models.CharField(max_length=150, blank=True, null=True)
    titulo = models.CharField(max_length=150, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

class UsuarioCampana(models.Model):
    usuario = models.ForeignKey(Usuario)
    campana = models.ForeignKey(Campana)
    push = models.IntegerField(blank=True, null=True)
    fecha_envio_campana = models.DateTimeField(blank=True, null=True)
    fecha_recibido_campana = models.DateTimeField(blank=True, null=True)
    fecha_ver_campana = models.DateTimeField(blank=True, null=True)
    fecha_abierto_campana = models.DateTimeField(blank=True, null=True)
    fecha_fin_campana = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

class RedWifiCampana(models.Model):
    campana = models.ForeignKey(Campana)
    router = models.ForeignKey(Router)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

class Telefono(models.Model):
    mac = models.CharField(max_length=45, blank=True, null=True)
    so = models.CharField(max_length=20, blank=True, null=True)
    device = models.CharField(max_length=100, blank=True, null=True)
    push = models.CharField(max_length=250, blank=True, null=True)
    nombre_telefono = models.CharField(max_length=250, blank=True, null=True)
    sdk = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)

class UsuarioTelefono(models.Model):
    usuario = models.ForeignKey(Usuario)
    telefono = models.ForeignKey(Telefono)
    redWifi = models.ForeignKey(RedWifi)
    status = models.IntegerField(blank=True, null=True)
    fecha_enlace_ini = models.DateTimeField(blank=True, null=True)
    fecha_enlace_fin = models.DateTimeField(blank=True, null=True)
    fecha_ult_conexion = models.DateTimeField(blank=True, null=True)

class CampoCampana(models.Model):
    campana = models.ForeignKey(Campana)
    campo_plantilla = models.ForeignKey(CampoPlantilla)
    valor = models.CharField(max_length=250, blank=True, null=True)
    valor_int = models.IntegerField(blank=True, null=True)

class Filtro(models.Model):
    campana = models.ForeignKey(Campana)
    filtro_etiqueta = models.ForeignKey(FiltroEtiqueta)
    valor = models.IntegerField(blank=True, null=True)
    operador = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

class ClientePlantilla(models.Model):
    cliente = models.ForeignKey(Cliente)
    plantilla = models.ForeignKey(Plantilla)
    status = models.IntegerField(blank=True, null=True)

class ActualizacionRouter(models.Model):
    actualizacion_router = models.AutoField(primary_key=True)
    redWifi = models.ForeignKey(RedWifi)
    comando = models.CharField(max_length=255, blank=True, null=True)
    fecha_lectura = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    router_key = models.CharField(db_column='ROUTER_KEY', max_length=32, blank=True, null=True)  # Field name made lowercase.

class RespuestaEncuesta(models.Model):
    encuesta = models.CharField(max_length=45, blank=True, null=True)
    usuario = models.ForeignKey(Usuario)
    valor_respuesta = models.CharField(db_column='_valor_respuesta', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fecha_encuesta = models.DateTimeField(db_column='_fecha_Encuesta', blank=True, null=True)  # Field name made lowercase.

class UsuarioPerfilEtiqueta(models.Model):
    tipo = models.CharField(max_length=20, blank=True, null=True)
    campo = models.CharField(max_length=200, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)

class UsuarioPerfil(models.Model):
    usuario = models.ForeignKey(Usuario)
    usuario_perfil_etiqueta = models.ForeignKey(UsuarioPerfilEtiqueta)
    dato = models.CharField(max_length=200, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)

class Administrador(models.Model):
    cliente = models.ForeignKey(Cliente)
    usuario = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    privilegio = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    login_status = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

class AdministradorLocal(models.Model):
    cliente = models.ForeignKey(Cliente)
    local = models.ForeignKey(Local)
    administrador = models.ForeignKey(Administrador)
"""