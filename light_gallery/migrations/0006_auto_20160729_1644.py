# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0005_auto_20160727_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightgallery',
            name='zoomActualSize',
            field=models.BooleanField(help_text=' \tEnable actual pixel icon', default=True, verbose_name='Actual Size'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='zoomEnableZoomAfter',
            field=models.PositiveIntegerField(help_text='Number in ms', default=50, verbose_name='Enable Zoom After'),
        ),
    ]
