# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 05:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import welcomehome.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('age', models.PositiveSmallIntegerField()),
                ('numberofKids', models.SmallIntegerField(default=0)),
                ('enrolldate', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=welcomehome.models.upload_location, width_field='width_field')),
                ('selfintroduction', models.TextField(default="I started hosting kids !! Let's cooperate her by sending warm greeting card")),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-enrolldate'],
            },
        ),
    ]