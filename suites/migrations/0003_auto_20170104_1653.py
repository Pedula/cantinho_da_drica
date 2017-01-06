# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suites', '0002_auto_20170104_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospede',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=100, verbose_name=b'Nome do cliente:')),
            ],
            options={
                'db_table': 'hospede',
                'verbose_name': 'Hospede',
                'verbose_name_plural': 'Hospedes',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='cliente',
        ),
        migrations.AddField(
            model_name='controlequarto',
            name='nomeCliente',
            field=models.ManyToManyField(to='suites.Hospede', verbose_name=b'Nome do Hospede:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nomequarto',
            name='nome',
            field=models.CharField(unique=True, max_length=30, verbose_name=b'Nome do quarto:'),
        ),
    ]
