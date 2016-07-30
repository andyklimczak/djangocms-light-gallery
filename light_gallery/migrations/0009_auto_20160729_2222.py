# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0008_auto_20160729_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightgallery',
            name='animateThumb',
            field=models.BooleanField(verbose_name='Enable Thumbnail Animation ', default=True),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='currentPagerPosition',
            field=models.CharField(max_length=255, help_text='Position of selected thumbnail', choices=[['left', 'left'], ['middle', 'middle'], ['right', 'right']], verbose_name='Current Pager Position', default='middle'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='enableThumbDrag',
            field=models.BooleanField(verbose_name='Enable Thumbnail Drag', help_text='Enables desktop mouse drag support for thumbnails', default=True),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='enableThumbSwipe',
            field=models.BooleanField(verbose_name='Enable Thumbnail Swipe', help_text='Enables thumbnail touch/swipe support for touch devices', default=True),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='pullCaptionUp',
            field=models.BooleanField(verbose_name='Pull Captions Up', help_text='Pull captions above thumbnails', default=True),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='thumbContHeight',
            field=models.PositiveIntegerField(help_text='Height of the thumbnail container including padding and border', verbose_name='Thumb Container Height', default=100),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='thumbMargin',
            field=models.PositiveIntegerField(help_text='Spacing between each thumbnails', verbose_name='Thumb Margin', default=5),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='thumbWidth',
            field=models.PositiveIntegerField(help_text='Width of each thumbnails', verbose_name='Thumb Width', default=100),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='toggleThumb',
            field=models.BooleanField(verbose_name='Toggle Thumbnail Button', help_text='Whether to display thumbnail toggle button', default=True),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='addClass',
            field=models.CharField(max_length=255, help_text='Add custom class for gallery, can be used to set different style for different gallery', verbose_name='Add Class', blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='nextHtml',
            field=models.CharField(max_length=255, help_text='Custom html for next control', verbose_name='Next Html', blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='preload',
            field=models.PositiveIntegerField(help_text='Number of preload slides. will execute only after the current slide is fully loaded', verbose_name='Preload', default=1),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='prevHtml',
            field=models.CharField(max_length=255, help_text='Custom html for prev control', verbose_name='Prev Html', blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='swipeThreshold',
            field=models.PositiveIntegerField(help_text='By setting the swipeThreshold (in px) you can set how far the user must swipe for the next/prev slide', verbose_name='Swipe Threshold', default=50),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='thumbnails',
            field=models.BooleanField(verbose_name='Enable Thumbnails', help_text='Enable/disable thumbnails for this gallery', default=True),
        ),
    ]
