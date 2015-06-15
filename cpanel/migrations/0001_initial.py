# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_campana', models.CharField(max_length=150, null=True, blank=True)),
                ('titulo', models.CharField(max_length=150, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=150, null=True, blank=True)),
                ('fecha_inicio', models.DateTimeField(null=True, blank=True)),
                ('fecha_fin', models.DateTimeField(null=True, blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('Activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campo', models.CharField(max_length=256)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cliente', models.CharField(max_length=45, null=True, blank=True)),
                ('email', models.EmailField(max_length=255, unique=True, null=True, blank=True)),
                ('rut', models.CharField(max_length=12, unique=True, null=True, blank=True)),
                ('logo', models.ImageField(help_text='50x50px image', upload_to='images/logos_clientes')),
                ('created', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('Activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RedWifi',
            fields=[
                ('ssid_key', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('mac', models.CharField(max_length=20, null=True, blank=True)),
                ('nas', models.IntegerField(null=True, blank=True)),
                ('updatedmac', models.CharField(max_length=20, null=True, blank=True)),
                ('updatedip', models.CharField(max_length=45, null=True, blank=True)),
                ('updatedproxyip', models.CharField(max_length=45, null=True, blank=True)),
                ('landing', models.URLField()),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('status', models.BooleanField(default=True)),
                ('metadata', models.CharField(max_length=255, null=True, blank=True)),
                ('cliente', models.ForeignKey(blank=True, to='cpanel.Cliente', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('router_key', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('name', models.CharField(default='sin asignar', max_length=255)),
                ('mac', models.CharField(max_length=20, null=True, blank=True)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('location', models.CharField(default='sin asignar', max_length=255)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('updatedmac', models.CharField(max_length=20, null=True, blank=True)),
                ('updatedip', models.CharField(max_length=45, null=True, blank=True)),
                ('updatedproxyip', models.CharField(max_length=45, null=True, blank=True)),
                ('metadata', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac', models.CharField(max_length=25, null=True, blank=True)),
                ('rssi', models.IntegerField(null=True, blank=True)),
                ('fecha_ingreso', models.DateTimeField(null=True, blank=True)),
                ('fecha_salida', models.DateTimeField(null=True, blank=True)),
                ('tiempo_conexion', models.IntegerField(null=True, blank=True)),
                ('current', models.IntegerField(null=True, blank=True)),
                ('ssid_key', models.CharField(max_length=32, null=True, blank=True)),
                ('router_key', models.CharField(max_length=32, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac', models.CharField(max_length=45, null=True, blank=True)),
                ('so', models.CharField(max_length=20, null=True, blank=True)),
                ('device', models.CharField(max_length=100, null=True, blank=True)),
                ('push', models.CharField(max_length=250, null=True, blank=True)),
                ('useragent', models.CharField(max_length=250, null=True, blank=True)),
                ('sdk', models.CharField(max_length=100, null=True, blank=True)),
                ('modelo', models.CharField(max_length=50, null=True, blank=True)),
                ('version', models.CharField(max_length=50, null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.EmailField(max_length=255, unique=True, null=True, blank=True)),
                ('password', models.CharField(max_length=50, null=True, blank=True)),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('sexo', models.IntegerField(null=True, blank=True)),
                ('fecha_nacimiento', models.DateField(null=True, blank=True)),
                ('email_notificacion', models.IntegerField(null=True, blank=True)),
                ('rut', models.CharField(max_length=10, null=True, blank=True)),
                ('msg_total', models.IntegerField(null=True, blank=True)),
                ('msg_send', models.IntegerField(null=True, blank=True)),
                ('sms_code', models.CharField(max_length=5, null=True, blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('Activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(default='sin asignar', max_length=255)),
                ('created', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('Activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='router',
            name='zona',
            field=models.ForeignKey(blank=True, to='cpanel.Zona', null=True),
        ),
        migrations.AddField(
            model_name='redwifi',
            name='router',
            field=models.ForeignKey(to='cpanel.Router'),
        ),
        migrations.AddField(
            model_name='campana',
            name='cliente',
            field=models.ForeignKey(to='cpanel.Cliente'),
        ),
    ]
