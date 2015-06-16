from django.shortcuts import render, render_to_response, RequestContext
import MySQLdb
import datetime

# Create your views here.

#def index_view(request):
#	return render_to_response('index.html', context=RequestContext(request))

def index_view(request):
	db = MySQLdb.connect(user='wifi_op',db='wifi_production',passwd='wifi_op',host='localhost')
	cursor = db.cursor()
	cursor.execute("""
		SELECT cpanel_redwifi.name, COUNT( cpanel_sesion.mac ) 
		FROM cpanel_sesion, cpanel_redwifi
		WHERE cpanel_redwifi.ssid_key = cpanel_sesion.redwifi_id
		GROUP BY cpanel_sesion.redwifi_id
		""")
	by_ssid = cursor.fetchall()
	cursor.execute("""
		SELECT cpanel_redwifi.name, COUNT( cpanel_sesion.mac ) 
		FROM cpanel_sesion, cpanel_redwifi
		WHERE cpanel_redwifi.ssid_key = cpanel_sesion.redwifi_id
		AND fecha_salida >= NOW() - INTERVAL 15 MINUTE
		GROUP BY cpanel_sesion.redwifi_id
		""")
	current_users = cursor.fetchall()
	cursor.execute("""
		SELECT cpanel_router.name, COUNT( cpanel_sesion.id ) 
		FROM cpanel_sesion, cpanel_redwifi, cpanel_router
		WHERE cpanel_router.router_key=cpanel_redwifi.router_id
		GROUP BY cpanel_redwifi.router_id
		""")
	by_router = cursor.fetchall()
	cursor.execute("""
		SELECT cpanel_redwifi.name, COUNT( DISTINCT(cpanel_sesion.mac) ) 
		FROM cpanel_sesion, cpanel_redwifi
		WHERE cpanel_redwifi.ssid_key = cpanel_sesion.redwifi_id
		GROUP BY cpanel_sesion.redwifi_id
		""")
	visitas_unicas_by_ssid = cursor.fetchall()
	cursor.execute("""
		SELECT cpanel_redwifi.name, COUNT( DISTINCT(cpanel_sesion.mac) ) 
		FROM cpanel_sesion, cpanel_redwifi
		WHERE cpanel_redwifi.ssid_key = cpanel_sesion.redwifi_id
		GROUP BY cpanel_sesion.redwifi_id
		""")
	visitas_totales_by_ssid = cursor.fetchall()
	cursor.execute("""
		SELECT cpanel_redwifi.name, round(SUM(cpanel_sesion.tiempo_conexion)/3600,2)
		FROM cpanel_sesion, cpanel_redwifi
		WHERE cpanel_redwifi.ssid_key = cpanel_sesion.redwifi_id
		GROUP BY cpanel_sesion.redwifi_id
		""")
	by_time = cursor.fetchall()
	cursor.execute("""
		SELECT cpanel_redwifi.name, ROUND((SUM(cpanel_sesion.tiempo_conexion)/3600)/COUNT(cpanel_sesion.id),2)
		FROM cpanel_sesion, cpanel_redwifi
		WHERE cpanel_redwifi.ssid_key = cpanel_sesion.redwifi_id
		GROUP BY cpanel_sesion.redwifi_id
		""")
	by_avg_visit_ssid = cursor.fetchall()
	cursor.execute("""
		SELECT cpanel_router.name, ROUND((SUM(cpanel_sesion.tiempo_conexion)/3600)/COUNT(cpanel_sesion.id),2)
		FROM cpanel_sesion, cpanel_redwifi, cpanel_router
		WHERE cpanel_router.router_key=cpanel_redwifi.router_id
		GROUP BY cpanel_redwifi.router_id
		""")
	by_avg_visit_router = cursor.fetchall()
	cursor.execute("""
		SELECT COUNT(id) 
		FROM cpanel_usuario
		""")
	usuarios_activos = cursor.fetchone()
	db.close()

	return render_to_response('index.html',{'by_ssid':by_ssid, 'by_router':by_router, 'by_time':by_time, 'usuarios_activos' :usuarios_activos, 'visitas_unicas_by_ssid' :visitas_totales_by_ssid, 'visitas_unicas_by_ssid' :visitas_totales_by_ssid, 'by_avg_visit_ssid' :by_avg_visit_ssid, 'by_avg_visit_router' :by_avg_visit_router, 'current_users' :current_users, 'time' : datetime.datetime.now()})
