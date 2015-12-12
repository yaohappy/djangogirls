# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundGet_101',
            fields=[
                ('index', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('year', models.IntegerField()),
                ('location', models.CharField(max_length=10)),
                ('org_name', models.CharField(max_length=30)),
                ('money', models.IntegerField()),
                ('content', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
