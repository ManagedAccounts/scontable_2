# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_auto_20150619_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordencompra',
            name='cantidad',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
    ]
