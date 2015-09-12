# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemforbarter',
            name='weight_units',
            field=models.CharField(default=None, choices=[('Ounces', 'oz'), ('Pounds', 'lbs'), ('Grams', 'g'), ('Kilograms', 'kg')], max_length=3),
            preserve_default=False,
        ),
    ]
