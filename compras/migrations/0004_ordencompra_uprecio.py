# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_ordencompra_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordencompra',
            name='uprecio',
            field=models.DecimalField(default=1, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
    ]
