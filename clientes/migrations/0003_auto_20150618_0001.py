# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20150617_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rod',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
