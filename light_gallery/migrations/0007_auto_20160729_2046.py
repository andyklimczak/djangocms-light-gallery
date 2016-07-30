# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0006_auto_20160729_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightgallery',
            name='mode',
            field=models.CharField(choices=[['lg-slide', 'lg-slide'], ['lg-fade', 'lg-fade'], ['lg-zoom-in', 'lg-zoom-in']], max_length=255, verbose_name='Mode', help_text='Type of transition between images', default='lg-slide'),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='zoomActualSize',
            field=models.BooleanField(help_text='Enable actual pixel icon', verbose_name='Actual Size', default=False),
        ),
    ]
