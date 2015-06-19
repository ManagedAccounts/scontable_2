# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20150618_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='pmarca',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
