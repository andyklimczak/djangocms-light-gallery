# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0009_auto_20160729_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightgallery',
            name='pager',
            field=models.BooleanField(default=False, verbose_name='Enable Pager', help_text='Enable/disable pager for this gallery'),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='currentPagerPosition',
            field=models.CharField(choices=[['left', 'Left'], ['middle', 'Middle'], ['right', 'Right']], default='middle', verbose_name='Current Pager Position', help_text='Position of selected thumbnail', max_length=255),
        ),
    ]
