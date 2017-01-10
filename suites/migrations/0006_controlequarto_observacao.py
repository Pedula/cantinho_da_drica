# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suites', '0005_controlequarto_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlequarto',
            name='observacao',
            field=models.TextField(null=True, verbose_name=b'Observa\xc3\xa7\xc3\xa3o', blank=True),
            preserve_default=True,
        ),
    ]
