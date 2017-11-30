# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_auto_20171130_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursesmodel1',
            old_name='course_subTitle',
            new_name='course_detail',
        ),
        migrations.RenameField(
            model_name='coursesmodel1',
            old_name='course_thumbanilImage',
            new_name='course_thumbnil_Image',
        ),
    ]
