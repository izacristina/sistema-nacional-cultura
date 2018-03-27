# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planotrabalho', '0006_auto_20180327_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conselhocultural',
            name='situacao_ata',
            field=models.ForeignKey(to='planotrabalho.SituacoesArquivoPlano', default=0),
        ),
        migrations.AlterField(
            model_name='fundocultura',
            name='situacao_lei_plano',
            field=models.ForeignKey(to='planotrabalho.SituacoesArquivoPlano', default=0),
        ),
        migrations.AlterField(
            model_name='orgaogestor',
            name='situacao_relatorio_secretaria',
            field=models.ForeignKey(to='planotrabalho.SituacoesArquivoPlano', default=0),
        ),
        migrations.AlterField(
            model_name='planocultura',
            name='situacao_lei_plano',
            field=models.ForeignKey(to='planotrabalho.SituacoesArquivoPlano', default=0),
        ),
    ]
