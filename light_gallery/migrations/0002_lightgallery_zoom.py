# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightgallery',
            name='zoom',
            field=models.BooleanField(default=False, help_text='Enable/disable zoom for this gallery', verbose_name='Zoom'),
        ),
    ]
