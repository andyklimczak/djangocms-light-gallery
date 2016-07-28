# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0002_lightgallery_zoom'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightgallery',
            name='fullscreen',
            field=models.BooleanField(default=False, verbose_name='Full screen', help_text='Enable/disable full screen for this gallery'),
        ),
    ]
