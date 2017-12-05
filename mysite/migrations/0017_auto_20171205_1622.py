# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_auto_20171204_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Email', models.EmailField(default=b'', max_length=100)),
                ('First_name', models.CharField(default=b'', max_length=100)),
                ('Last_name', models.CharField(default=b'', max_length=100)),
                ('Password', models.CharField(default=b'', max_length=100)),
                ('Confirm_password', models.CharField(default=b'', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
