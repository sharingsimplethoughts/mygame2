# Generated by Django 2.2.6 on 2020-05-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_auto_20200508_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentplayermanager',
            name='total_games_drawn',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
