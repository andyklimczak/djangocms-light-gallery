# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0013_auto_20170617_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightgallery',
            name='showThumbByDefault',
            field=models.BooleanField(default=True, verbose_name='Show/Hide thumbnails by default'),
        ),
    ]
