# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0003_lightgallery_fullscreen'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightgallery',
            name='thumbnails',
            field=models.BooleanField(default=False, help_text='Enable/disable thumbnails for this gallery', verbose_name='Thumbnails'),
        ),
    ]
