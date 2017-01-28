# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suites', '0007_auto_20170116_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlequarto',
            name='forma_pagamento',
            field=models.PositiveSmallIntegerField(default=None, null=True, verbose_name=b'Forma de pagamento:', blank=True, choices=[(1, 'Dinheiro'), (2, 'Cart\xe3o de cr\xe9dito'), (3, 'Cart\xe3o de d\xe9bito')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='controlequarto',
            name='vendedor',
            field=models.PositiveSmallIntegerField(default=1, choices=[(6, 'Garnize'), (3, 'Renato'), (1, 'Ivo'), (2, 'Sandra'), (4, 'Renan'), (5, 'Viviane'), (7, 'Outros')]),
        ),
    ]
