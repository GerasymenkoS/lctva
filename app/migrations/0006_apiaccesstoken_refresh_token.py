# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_apikey_redirect_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiaccesstoken',
            name='refresh_token',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
