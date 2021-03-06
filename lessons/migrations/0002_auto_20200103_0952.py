# Generated by Django 2.2.6 on 2020-01-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='videopreviewurl',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='videourl',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='lessoncategory',
            name='iconurl',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
