# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_ordencompra_uprecio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordencompra',
            old_name='ocompra',
            new_name='ccompra',
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='tcomprobante',
            field=models.CharField(default=2, max_length=2, choices=[(b'01', b'Factura'), (b'03', b'Boleta de Venta'), (b'07', b'Nota de Credito'), (b'08', b'Nota de Debito'), (b'60', b'Control Interno')]),
            preserve_default=False,
        ),
    ]
