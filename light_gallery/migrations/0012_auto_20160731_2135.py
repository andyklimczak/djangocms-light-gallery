# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0011_auto_20160731_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightgallery',
            name='galleryId',
            field=models.PositiveIntegerField(help_text='Unique id for each gallery. It is mandatory when you use hash plugin for multiple galleries on the same page', verbose_name='Gallery Id', default=1),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='hash',
            field=models.BooleanField(help_text='Enable/Disable hash plugin', verbose_name='Enable Hash', default=False),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='pageThumbWidth',
            field=models.CharField(help_text='Width of thumbnail on page', verbose_name='Page Thumb Width', max_length=255, default='150'),
        ),
    ]
