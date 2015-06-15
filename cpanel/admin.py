from django.contrib import admin 
from django.contrib.admin import AdminSite

# Register your models here.
from .models import Usuario, Campana, Telefono, Router, Sesion, Cliente, Zona, RedWifi, Campo



class UsuarioAdmin(admin.ModelAdmin):
	list_display = ['email', 'rut']
	search_fields = ['email']
	readonly_fields = ['created']

class RouterAdmin(admin.ModelAdmin):
	#exclude = ['location']
	readonly_fields = ['router_key','mac','created','updated','updatedmac','updatedip','updatedproxyip']
	list_display = ['router_key','name','location']
	list_filter = ['name','location']
	#filter_horizontal = ['campanas']

class ClienteAdmin(admin.ModelAdmin):
	readonly_fields = ['created']
	list_display = ['email']
	list_filter = ['email']
	
class RedWifiAdmin(admin.ModelAdmin):
	readonly_fields = ['ssid_key','mac','name','created','updated','updatedmac','updatedip','updatedproxyip']
	list_display = ['name']
	list_filter = ['name']
	#filter_horizontal = ['campanas']

class SesionAdmin(admin.ModelAdmin):
	readonly_fields = ['mac','rssi','fecha_ingreso','fecha_salida','tiempo_conexion', 'current']
	exclude = ['router_key_id','ssid_key_id']
	list_display = ['mac', 'tiempo_conexion']
	list_filter = ['mac']

class ZonaAdmin(admin.ModelAdmin):
	readonly_fields = ['created']
	list_display = ['nombre']
	list_filter = ['nombre']
	#filter_horizontal = ['campanas']

class CampanaAdmin(admin.ModelAdmin):
	readonly_fields = ['created']
	list_display = ['nombre_campana', 'titulo']
	list_filter = ['nombre_campana']

class TelefonoAdmin(admin.ModelAdmin):
	readonly_fields = ['created']
	list_display = ['mac', 'so']
	list_filter = ['so']

class CampoAdmin(admin.ModelAdmin):
	list_display = ['campo']
	

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Router, RouterAdmin)
admin.site.register(Sesion, SesionAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Zona, ZonaAdmin)
admin.site.register(RedWifi, RedWifiAdmin)
admin.site.register(Campana, CampanaAdmin)
admin.site.register(Telefono, TelefonoAdmin)
admin.site.register(Campo, CampoAdmin)

AdminSite.site_title 	= 	'Wifi-Gratis'			#<title>
AdminSite.site_header 	= 	AdminSite.site_title 	#<h1 id="site-name">Panel de control</a></h1>
AdminSite.index_title	=	'Panel de control'		#content <h1>Panel de control</h1>
