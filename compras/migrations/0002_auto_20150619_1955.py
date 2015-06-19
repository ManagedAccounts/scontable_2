# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordencompra',
            name='tpago',
            field=models.CharField(max_length=1, choices=[(b'e', b'Efectivo'), (b'c', b'Credito')]),
        ),
    ]
