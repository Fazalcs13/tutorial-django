# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0017_auto_20171205_1622'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddCourses',
            new_name='Courses',
        ),
    ]
