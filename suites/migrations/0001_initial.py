# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ControleQuarto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_inicio', models.DateTimeField(null=True, blank=True)),
                ('data_fim', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'ControleQuarto',
                'verbose_name': 'Controle do quarto',
                'verbose_name_plural': 'Controle dos quartos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NomeQuarto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'db_table': 'NomeQuarto',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='controlequarto',
            name='NomeQuartos',
            field=models.ManyToManyField(to='suites.NomeQuarto', null=True, blank=True),
            preserve_default=True,
        ),
    ]
