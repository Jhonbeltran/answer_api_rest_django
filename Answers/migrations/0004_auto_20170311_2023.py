# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Answers', '0003_auto_20170311_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='change_pass_answer',
            field=models.IntegerField(),
        ),
    ]