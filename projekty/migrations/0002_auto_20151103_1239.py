# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projekty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projekt',
            name='liczba_miejsc',
            field=models.IntegerField(verbose_name=b'Lb. miejsc'),
        ),
    ]
