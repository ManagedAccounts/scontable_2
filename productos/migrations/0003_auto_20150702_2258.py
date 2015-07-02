# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20150702_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='procompra',
            field=models.ForeignKey(to='proveedores.Proveedor'),
        ),
    ]
