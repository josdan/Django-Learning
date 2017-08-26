# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_more_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(null=True, max_length=254),
        ),
    ]
