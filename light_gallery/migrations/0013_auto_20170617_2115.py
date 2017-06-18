# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0012_auto_20160731_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lightgallery',
            name='enableTouch',
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='enableSwipe',
            field=models.BooleanField(default=True, help_text='Enables swipe support', verbose_name='Enable Swipe'),
        ),
        migrations.AlterField(
            model_name='lightgallery',
            name='cmsplugin_ptr',
            field=models.OneToOneField(related_name='light_gallery_lightgallery', serialize=False, to='cms.CMSPlugin', primary_key=True, parent_link=True, auto_created=True),
        ),
    ]
