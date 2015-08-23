# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemForBarter',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('length', models.FloatField()),
                ('length_units', models.CharField(max_length=3, choices=[('Inches', 'in'), ('Feet', 'ft'), ('Yards', 'yd'), ('Miles', 'mi'), ('Millimeters', 'mm'), ('Centimeters', 'cm'), ('Meters', 'm'), ('Kilometers', 'km')])),
                ('width', models.FloatField()),
                ('width_units', models.CharField(max_length=3, choices=[('Inches', 'in'), ('Feet', 'ft'), ('Yards', 'yd'), ('Miles', 'mi'), ('Millimeters', 'mm'), ('Centimeters', 'cm'), ('Meters', 'm'), ('Kilometers', 'km')])),
                ('height', models.FloatField()),
                ('height_units', models.CharField(max_length=3, choices=[('Inches', 'in'), ('Feet', 'ft'), ('Yards', 'yd'), ('Miles', 'mi'), ('Millimeters', 'mm'), ('Centimeters', 'cm'), ('Meters', 'm'), ('Kilometers', 'km')])),
                ('weight', models.FloatField()),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
