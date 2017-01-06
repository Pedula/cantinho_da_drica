# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suites', '0003_auto_20170104_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='controlequarto',
            old_name='nomeCliente',
            new_name='nomeHospede',
        ),
    ]
