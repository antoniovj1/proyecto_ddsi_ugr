# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-06 09:33
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gestion_clientes', '0002_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('descripcion', models.CharField(blank=True, max_length=150, null=True)),
                ('diagnostico', models.CharField(blank=True, max_length=150, null=True)),
                ('plan', models.CharField(blank=True, max_length=150, null=True)),
                ('oculista', models.CharField(blank=True, max_length=50, null=True)),
                ('cliente_rev',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_clientes.Cliente')),
            ],
        ),
    ]
