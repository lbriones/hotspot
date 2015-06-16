# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpanel', '0002_remove_redwifi_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sesion',
            name='ssid_key',
            field=models.ForeignKey(blank=True, to='cpanel.RedWifi', null=True),
        ),
    ]
