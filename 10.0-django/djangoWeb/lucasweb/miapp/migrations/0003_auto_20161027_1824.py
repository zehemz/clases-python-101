# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 18:24
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=''),
        ),
    ]