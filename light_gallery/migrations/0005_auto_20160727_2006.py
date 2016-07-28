# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0004_lightgallery_thumbnails'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightgallery',
            name='zoomScale',
            field=models.PositiveIntegerField(default=1, help_text='Value of zoom should be incremented/decremented', verbose_name='Scale'),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='fullscreen',
            field=models.BooleanField(default=False, help_text='Enable/disable fullscreen for this gallery', verbose_name='Enable Fullscreen'),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='thumbnails',
            field=models.BooleanField(default=False, help_text='Enable/disable thumbnails for this gallery', verbose_name='Enable Thumbnails'),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='zoom',
            field=models.BooleanField(default=False, help_text='Enable/disable zoom for this gallery', verbose_name='Enable Zoom'),
        ),
    ]
