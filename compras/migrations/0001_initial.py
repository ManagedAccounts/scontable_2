# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20150619_1951'),
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordencompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ocompra', models.PositiveIntegerField()),
                ('tpago', models.PositiveIntegerField(choices=[(b'e', b'Efectivo'), (b'c', b'Credito')])),
                ('fecha', models.DateTimeField()),
                ('descripcion', models.TextField()),
                ('aproucto', models.ForeignKey(to='productos.Producto')),
                ('pcompra', models.ForeignKey(to='proveedores.Proveedor')),
            ],
        ),
    ]
