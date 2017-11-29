# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesModel1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_thumbanilImage', models.ImageField(null=True, upload_to=b'static', blank=True)),
                ('course_title', models.TextField()),
                ('course_subTitle', models.TextField()),
                ('course_author_image', models.ImageField(null=True, upload_to=b'static', blank=True)),
                ('course_author_name', models.TextField()),
                ('course_date', models.TextField()),
                ('course_duration', models.TextField()),
            ],
        ),
    ]
