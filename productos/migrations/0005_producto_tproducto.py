# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20150619_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tproducto',
            field=models.CharField(default=2, max_length=2, choices=[(b'01', b'Mercaderia'), (b'02', b'Producto Terminado'), (b'03', b'Materias Primas y Auxiliares'), (b'04', b'Envases y Envalajes'), (b'05', b'Suministros Diversos'), (b'06', b'Inmueble Maquinaria y Equipo')]),
            preserve_default=False,
        ),
    ]
