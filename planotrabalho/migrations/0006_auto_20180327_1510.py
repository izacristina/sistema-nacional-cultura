# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planotrabalho', '0005_auto_20180327_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criacaosistema',
            name='situacao_lei_sistema',
            field=models.ForeignKey(default=0, to='planotrabalho.SituacoesArquivoPlano'),
        ),
    ]
