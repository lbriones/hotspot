# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpanel', '0004_auto_20150615_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sesion',
            old_name='ssid_key',
            new_name='redwifi',
        ),
        migrations.RenameField(
            model_name='sesion',
            old_name='router_key',
            new_name='router',
        ),
    ]
