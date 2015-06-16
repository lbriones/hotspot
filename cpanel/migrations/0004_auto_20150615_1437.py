# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpanel', '0003_auto_20150615_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sesion',
            name='router_key',
            field=models.ForeignKey(blank=True, to='cpanel.Router', null=True),
        ),
    ]
