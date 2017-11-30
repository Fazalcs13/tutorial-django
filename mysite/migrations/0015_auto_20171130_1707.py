# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_auto_20171130_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesmodel1',
            name='course_thumbnil_Image',
            field=models.ImageField(upload_to=b''),
        ),
    ]
