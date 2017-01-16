# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suites', '0006_controlequarto_observacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='controlequarto',
            options={'ordering': ('-data_inicio',), 'verbose_name': 'Controle do quarto', 'verbose_name_plural': 'Controle dos quartos'},
        ),
        migrations.AlterModelOptions(
            name='hospede',
            options={'ordering': ['nome'], 'verbose_name': 'Hospede', 'verbose_name_plural': 'Hospedes'},
        ),
        migrations.AlterModelOptions(
            name='nomequarto',
            options={'ordering': ['nome'], 'verbose_name': 'nome do quarto', 'verbose_name_plural': 'nome dos quartos'},
        ),
        migrations.AddField(
            model_name='controlequarto',
            name='vendedor',
            field=models.PositiveSmallIntegerField(default=1, choices=[(6, 'Garnize'), (3, 'Renato'), (1, 'Ivo'), (2, 'Sandra'), (4, 'Renan'), (5, 'Viviane')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='controlequarto',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, choices=[(1, 'Negociando'), (3, 'Reservado'), (2, 'Fechado'), (4, 'Cancelado')]),
        ),
    ]
