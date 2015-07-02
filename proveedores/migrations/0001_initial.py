# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rsocial', models.CharField(max_length=101)),
                ('rod', models.PositiveSmallIntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('toc', models.PositiveSmallIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('contacto', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
