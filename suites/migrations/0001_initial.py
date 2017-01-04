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
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('diaria', models.IntegerField(null=True, blank=True)),
                ('qtd_dias', models.IntegerField(null=True, blank=True)),
                ('valor_reserva', models.FloatField(null=True, blank=True)),
                ('valor_total', models.FloatField(null=True, blank=True)),
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
                'verbose_name': 'nome do quarto',
                'verbose_name_plural': 'nome dos quartos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='controlequarto',
            name='nomeQuartos',
            field=models.ManyToManyField(to='suites.NomeQuarto'),
            preserve_default=True,
        ),
    ]
