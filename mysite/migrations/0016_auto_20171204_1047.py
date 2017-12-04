# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0015_auto_20171130_1707'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoursesModel1',
            new_name='AddCourses',
        ),
        migrations.RemoveField(
            model_name='user',
            name='UserName',
        ),
        migrations.AddField(
            model_name='user',
            name='Confirm_password',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='Email',
            field=models.EmailField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='First_name',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='Last_name',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='Password',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
