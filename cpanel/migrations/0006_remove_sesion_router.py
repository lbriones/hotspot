# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpanel', '0005_auto_20150615_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sesion',
            name='router',
        ),
    ]
