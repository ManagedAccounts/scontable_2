# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_producto_pmarca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='pmarca',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
