# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_coursesmodel1_course_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_thumbanilImage', models.ImageField(upload_to=b'')),
                ('course_title', models.TextField()),
                ('course_subTitle', models.TextField()),
            ],
        ),
    ]
