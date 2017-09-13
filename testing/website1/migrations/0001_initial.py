# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import website1.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('workout', models.CharField(max_length=120, null=True, validators=[website1.validators.validate_workout])),
                ('timestamp', models.DateTimeField(null=True)),
                ('weight', models.FloatField(max_length=5, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
