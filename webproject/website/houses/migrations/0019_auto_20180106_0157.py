# Generated by Django 2.1.dev20171223092632 on 2018-01-06 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0018_houses_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='houses',
        ),
        migrations.DeleteModel(
            name='house',
        ),
    ]