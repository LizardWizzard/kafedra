# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=2, unique=True, verbose_name='Курс')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Этап обучения')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название предмета')),
                ('description', models.TextField(verbose_name='Описание предмета')),
            ],
        ),
        migrations.AddField(
            model_name='kurs',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Step'),
        ),
    ]
