# Generated by Django 2.1.dev20171223092632 on 2018-01-06 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0012_remove_houses_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]