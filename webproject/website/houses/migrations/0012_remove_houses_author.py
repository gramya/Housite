# Generated by Django 2.1.dev20171223092632 on 2018-01-06 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0011_auto_20180106_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houses',
            name='author',
        ),
    ]