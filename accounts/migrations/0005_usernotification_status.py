# Generated by Django 2.2.6 on 2019-12-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_usernotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernotification',
            name='status',
            field=models.CharField(choices=[('1', 'active'), ('2', 'inactive'), ('3', 'expired')], default='1', max_length=50),
        ),
    ]