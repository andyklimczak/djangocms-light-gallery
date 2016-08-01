# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0010_auto_20160729_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightgallery',
            name='pageThumbHeight',
            field=models.CharField(verbose_name='Page Thumb Height', max_length=255, default='150', help_text='Height of thumbnail on page'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='pageThumbWidth',
            field=models.CharField(verbose_name='Page Thumb Width', max_length=255, default='150', help_text='Width of thumbnial on page'),
        ),
    ]
