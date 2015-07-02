# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='procompra',
            field=models.OneToOneField(default=2, to='proveedores.Proveedor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='pcompra',
            field=models.DecimalField(max_digits=20, decimal_places=2),
        ),
    ]
