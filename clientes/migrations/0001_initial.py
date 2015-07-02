# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rsocial', models.CharField(max_length=100)),
                ('tcliente', models.SmallIntegerField(choices=[(0, b'Juridica'), (1, b'Natural')])),
                ('rod', models.PositiveSmallIntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('toc', models.PositiveSmallIntegerField()),
                ('estado', models.SmallIntegerField(choices=[(0, b'Activo'), (1, b'Inactivo')])),
            ],
        ),
    ]
