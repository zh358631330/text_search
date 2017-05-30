# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('aid', models.IntegerField(serialize=False, primary_key=True)),
                ('atitle', models.CharField(max_length=20, null=True, blank=True)),
                ('pid', models.IntegerField(null=True, verbose_name='self', blank=True)),
            ],
            options={
                'db_table': 'areas',
            },
        ),
    ]
