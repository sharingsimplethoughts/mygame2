# Generated by Django 2.2.6 on 2020-01-03 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_notificationgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernotification',
            name='req_type',
            field=models.CharField(choices=[('1', 'friend request'), ('2', 'game request'), ('3', 'from admin')], default='1', max_length=50),
        ),
    ]