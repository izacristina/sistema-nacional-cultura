# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planotrabalho', '0003_migra_arquivos_componentes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conselhocultural',
            name='data_envio',
            field=models.DateField(editable=False),
        ),
        migrations.AlterField(
            model_name='criacaosistema',
            name='data_envio',
            field=models.DateField(editable=False),
        ),
        migrations.AlterField(
            model_name='fundocultura',
            name='data_envio',
            field=models.DateField(editable=False),
        ),
        migrations.AlterField(
            model_name='orgaogestor',
            name='data_envio',
            field=models.DateField(editable=False),
        ),
        migrations.AlterField(
            model_name='planocultura',
            name='data_envio',
            field=models.DateField(editable=False),
        ),
    ]
