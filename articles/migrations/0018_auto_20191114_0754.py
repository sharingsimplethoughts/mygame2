# Generated by Django 2.2.6 on 2019-11-14 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_videocategory_is_blocked'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocategory',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='videos/category'),
        ),
        migrations.AddField(
            model_name='videocategory',
            name='icon_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
