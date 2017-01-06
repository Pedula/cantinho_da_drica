# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'db_table': 'cliente',
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='controlequarto',
            name='data_fim',
            field=models.DateTimeField(verbose_name=b'Data de sa\xc3\xadda'),
        ),
        migrations.AlterField(
            model_name='controlequarto',
            name='data_inicio',
            field=models.DateTimeField(verbose_name=b'Data de entrada:'),
        ),
        migrations.AlterField(
            model_name='controlequarto',
            name='diaria',
            field=models.IntegerField(null=True, verbose_name=b'Valor da di\xc3\xa1ria', blank=True),
        ),
        migrations.AlterField(
            model_name='controlequarto',
            name='nomeQuartos',
            field=models.ManyToManyField(to=b'suites.NomeQuarto', verbose_name=b'Nome do quarto:'),
        ),
        migrations.AlterField(
            model_name='controlequarto',
            name='qtd_dias',
            field=models.FloatField(null=True, verbose_name=b'Quantidade de dias:', blank=True),
        ),
        migrations.AlterField(
            model_name='controlequarto',
            name='valor_reserva',
            field=models.FloatField(null=True, verbose_name=b'valor da reserva:', blank=True),
        ),
        migrations.AlterField(
            model_name='controlequarto',
            name='valor_total',
            field=models.FloatField(null=True, verbose_name=b'valor total:', blank=True),
        ),
    ]
