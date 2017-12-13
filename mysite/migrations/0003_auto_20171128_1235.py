# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_coursesmodel1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesmodel1',
            name='course_author_image',
            field=models.ImageField(null=True, upload_to=b'http://127.0.0.1:8000/static/images', blank=True),
        ),
        migrations.AlterField(
            model_name='coursesmodel1',
            name='course_thumbanilImage',
            field=models.ImageField(null=True, upload_to=b'http://127.0.0.1:8000/static/images', blank=True),
        ),
    ]
