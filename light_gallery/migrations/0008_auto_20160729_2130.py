# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0007_auto_20160729_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightgallery',
            name='addClass',
            field=models.CharField(default='', max_length=255, help_text='Add custom class for gallery, can be used to set different style for different gallery', verbose_name='Add Class'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='appendCounterTo',
            field=models.CharField(default='.lg-toolbar', max_length=255, help_text='Where the counter should be appended', verbose_name='Append Counter To'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='backdropDuration',
            field=models.PositiveIntegerField(default=150, help_text='Lightgallery backdrop transtion duration. Do not change the value of backdrop via css', verbose_name='Backdrop Duration'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='closable',
            field=models.BooleanField(default=True, verbose_name='Closable', help_text='Allows clicks on dimmer to close gallery'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='controls',
            field=models.BooleanField(default=True, verbose_name='Controls', help_text='If false, prev/next buttons will not be displayed'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='counter',
            field=models.BooleanField(default=True, verbose_name='Counter', help_text='Whether to show total number of images and index number of currently displayed image'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='cssEasing',
            field=models.CharField(default='ease', max_length=255, help_text='Type of easing to be used for css animations', verbose_name='CSS Easing'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='download',
            field=models.BooleanField(default=True, verbose_name='Download', help_text='Enable download button'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='easing',
            field=models.CharField(default='linear', max_length=255, help_text='Type of easing to be used for jquery animations', verbose_name='Easing'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='enableDrag',
            field=models.BooleanField(default=True, verbose_name='Enable Drag', help_text='Enables desktop mouse drag support'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='enableTouch',
            field=models.BooleanField(default=True, verbose_name='Enable Touch', help_text='Enables touch support'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='escKey',
            field=models.BooleanField(default=True, verbose_name='ESC Key', help_text="Whether the LightGallery could be closed by pressing the 'Esc' key"),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='height',
            field=models.CharField(default='100%', max_length=255, help_text='Height of the gallery', verbose_name='Height'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='hideBarsDelay',
            field=models.PositiveIntegerField(default=6000, help_text='Delay for hiding gallery controls in ms', verbose_name='Hide Bars Delay'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='hideControlOnEnd',
            field=models.BooleanField(default=False, verbose_name='Hide Control On End', help_text='If true, prev/next button will be hidden on first/last image'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='iframeMaxWidth',
            field=models.CharField(default='100%', max_length=255, help_text='Set maximum width for iframe.', verbose_name='IFrame Max Width'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='index',
            field=models.PositiveIntegerField(default=0, help_text='Allows to set which image/video should load initially', verbose_name='Index'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='keyPress',
            field=models.BooleanField(default=True, verbose_name='Key Press', help_text='Enable keyboard navigation'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='loop',
            field=models.BooleanField(default=True, verbose_name='Loop', help_text='If false, will disable the ability to loop back to the beginning of the gallery when on the last element'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='mousewheel',
            field=models.BooleanField(default=True, verbose_name='Mousewheel', help_text='Change slide on mousewheel'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='nextHtml',
            field=models.CharField(default='', max_length=255, help_text='Custom html for next control', verbose_name='Next Html'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='preload',
            field=models.PositiveIntegerField(default=1, help_text='Number of preload slides. will exicute only after the current slide is fully loaded', verbose_name='Preload'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='prevHtml',
            field=models.CharField(default='', max_length=255, help_text='Custom html for prev control', verbose_name='Prev Html'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='showAfterLoad',
            field=models.BooleanField(default=True, verbose_name='Show After Load', help_text='Show Content once it is fully loaded'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='slideEndAnimation',
            field=models.BooleanField(default=True, verbose_name='Slide End Animation', help_text='Enable slideEnd animation'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='speed',
            field=models.PositiveIntegerField(default=600, help_text='Transition duration (in ms)', verbose_name='Speed'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='startClass',
            field=models.CharField(default='lg-start-zoom', max_length=255, help_text='Starting animation class for the gallery', verbose_name='Add Class'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='swipeThreshold',
            field=models.PositiveIntegerField(default=50, help_text='By setting the swipeThreshold (in px) you can set how far the user must swipe for the next/prev image', verbose_name='Swipe Threshold'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='useLeft',
            field=models.BooleanField(default=False, verbose_name='Use Left', help_text='Force lightgallery to use css left property instead of transform'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='width',
            field=models.CharField(default='100%', max_length=255, help_text='Width of the gallery', verbose_name='Width'),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='mode',
            field=models.CharField(default=['lg-slide', 'lg-slide'], max_length=255, choices=[['lg-slide', 'lg-slide'], ['lg-fade', 'lg-fade'], ['lg-zoom-in', 'lg-zoom-in'], ['lg-zoom-in-big', 'lg-zoom-in-big'], ['lg-zoom-out', 'lg-zoom-out'], ['lg-zoom-out-big', 'lg-zoom-out-big'], ['lg-zoom-out-in', 'lg-zoom-out-in'], ['lg-zoom-in-out', 'lg-zoom-in-out'], ['lg-soft-zoom', 'lg-soft-zoom'], ['lg-scale-up', 'lg-scale-up'], ['lg-slide-circular', 'lg-slide-circular'], ['lg-slide-circular-vertical', 'lg-slide-circular-vertical'], ['lg-slide-vertical', 'lg-slide-vertical'], ['lg-slide-vertical-growth', 'lg-slide-vertical-growth'], ['lg-slide-skew-only', 'lg-slide-skew-only'], ['lg-slide-skew-only-rev', 'lg-slide-skew-only-rev'], ['lg-slide-skew-only-y', 'lg-slide-skew-only-y'], ['lg-slide-skew-only-y-rev', 'lg-slide-skew-only-y-rev'], ['lg-slide-skew', 'lg-slide-skew'], ['lg-slide-skew-rev', 'lg-slide-skew-rev'], ['lg-slide-skew-cross', 'lg-slide-skew-cross'], ['lg-slide-skew-cross-rev', 'lg-slide-skew-cross-rev'], ['lg-slide-skew-ver', 'lg-slide-skew-ver'], ['lg-slide-skew-ver-rev', 'lg-slide-skew-ver-rev'], ['lg-slide-skew-ver-cross', 'lg-slide-skew-ver-cross'], ['lg-slide-skew-ver-cross-rev', 'lg-slide-skew-ver-cross-rev'], ['lg-lollipop', 'lg-lollipop'], ['lg-lollipop-rev', 'lg-lollipop-rev'], ['lg-rotate', 'lg-rotate'], ['lg-rotate-rev', 'lg-rotate-rev'], ['lg-tube', 'lg-tube']], help_text='Type of transition between images', verbose_name='Mode'),
        ),
    ]
