# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_auto_20171130_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesmodel1',
            name='course_thumbnil_Image',
            field=models.ImageField(height_field=b'502', width_field=b'731', upload_to=b''),
        ),
    ]
