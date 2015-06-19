# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20150619_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ruc', models.IntegerField()),
                ('razon_social', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tabla_10', models.CharField(default=1, max_length=2, choices=[(b'00', b'otros'), (b'01', b'Factura'), (b'02', b'Recibo por honorarios'), (b'03', b'Boleta'), (b'04', b'Liquidacion de compra'), (b'05', b'Boleto de compa\xc3\xb1ia de aviacion comercial por el transporte aereo de pasajeros'), (b'06', b'carta de porte a\xc3\xa9reo'), (b'07', b'Nota de cr\xc3\xa9dito'), (b'08', b'Nota de d\xc3\xa9bito'), (b'09', b'Guia de remisi\xc3\xb3n'), (b'10', b'Recibo por arrendamiento'), (b'11', b'P\xc3\xb3liza emitida por las bolsas de Valores, Bolsas de productos o agentes de intermediacion por operaciones realizadas en bolsas de valores o productos fuera de las mismas, autorizadas por CONASEV'), (b'12', b'Ticket o cinta emitido por maquina registradora'), (b'13', b'Documento emitido por bancos, instituciones financieras, crediticias y de seguros que se encuenten bajo el de la Superintendencia de Banca y Seguros'), (b'14', b'Recibo por servicios p\xc3\xbablicos de suministro de energ\xc3\xada el\xc3\xa9ctrica, agua, tel\xc3\xa9fono, telex y tlegr\xc3\xa1ficos y otros, servicios complementarios que se incluyan en el recibo de servicio p\xc3\xbablico'), (b'15', b'Boleto emitido por las empresas de transporte p\xc3\xbablico urbano de pasajeros')])),
                ('num_factura', models.IntegerField()),
                ('num_boleta', models.IntegerField()),
                ('fecha', models.DateField()),
                ('igv', models.FloatField(default=0.0)),
                ('total', models.FloatField(default=0.0)),
                ('cliente', models.ForeignKey(to='ventas.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('importe', models.FloatField(default=0.0)),
                ('articulo', models.ForeignKey(to='productos.Producto')),
                ('comprobante', models.ForeignKey(to='ventas.Comprobante')),
            ],
        ),
    ]
