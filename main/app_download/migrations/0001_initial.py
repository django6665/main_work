# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xlsx', models.FileField(upload_to='%m/%d')),
                ('now', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
