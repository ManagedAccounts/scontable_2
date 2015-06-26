# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comprobante',
            old_name='num_boleta',
            new_name='numero',
        ),
        migrations.RenameField(
            model_name='comprobante',
            old_name='num_factura',
            new_name='serie',
        ),
    ]
