# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suites', '0004_auto_20170104_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlequarto',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, choices=[(1, 'Negociando'), (2, 'Fechado')]),
            preserve_default=True,
        ),
    ]
