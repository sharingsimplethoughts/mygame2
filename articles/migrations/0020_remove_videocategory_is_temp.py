# Generated by Django 2.2.6 on 2019-11-14 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_videocategory_is_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videocategory',
            name='is_temp',
        ),
    ]
