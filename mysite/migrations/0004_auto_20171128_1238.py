# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20171128_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesmodel1',
            name='course_author_image',
            field=models.ImageField(null=True, upload_to=b'static/images', blank=True),
        ),
        migrations.AlterField(
            model_name='coursesmodel1',
            name='course_thumbanilImage',
            field=models.ImageField(null=True, upload_to=b'static/images', blank=True),
        ),
    ]
