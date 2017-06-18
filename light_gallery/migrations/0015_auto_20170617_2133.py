# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_gallery', '0014_lightgallery_showthumbbydefault'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightgallery',
            name='facebook',
            field=models.BooleanField(verbose_name='Enable Facebook share', default=True),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='facebookDropdownText',
            field=models.CharField(verbose_name='Facebook dropdown text', max_length=255, default='Facebook'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='googlePlus',
            field=models.BooleanField(verbose_name='Enable googlePlus share', default=True),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='googlePlusDropdownText',
            field=models.CharField(verbose_name='GooglePlus dropdown text', max_length=255, default='GooglePlus'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='pinterest',
            field=models.BooleanField(verbose_name='Enable Pinterest share', default=True),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='pinterestDropdownText',
            field=models.CharField(verbose_name='Pinterest dropdown text', max_length=255, default='Pinterest'),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='share',
            field=models.BooleanField(verbose_name='Enable/Disable share plugin', default=True),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='twitter',
            field=models.BooleanField(verbose_name='Enable Twitter share', default=True),
        ),
        migrations.AddField(
            model_name='lightgallery',
            name='twitterDropdownText',
            field=models.CharField(verbose_name='Twitter dropdown text', max_length=255, default='Twitter'),
        ),
    ]
