# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.folder


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('filer', '0006_auto_20160623_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightGallery',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', parent_link=True, primary_key=True, auto_created=True, serialize=False)),
                ('folder', filer.fields.folder.FilerFolderField(to='filer.Folder', verbose_name='Folder')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
