# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_auto_20171128_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesmodel1',
            name='course_category',
            field=models.CharField(default=b'MOS', max_length=5, choices=[(b'MOS', b'Microsoft Office Suite'), (b'GD', b'Graphic Design'), (b'SM', b'Sound & Music'), (b'WD', b'Web Site Development'), (b'AP', b'Animation Production'), (b'VE', b'Video Editing')]),
        ),
    ]
