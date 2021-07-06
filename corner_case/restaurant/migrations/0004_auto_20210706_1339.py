# Generated by Django 3.1.12 on 2021-07-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20210706_1337'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='menu',
            name='same day menu',
        ),
        migrations.AddConstraint(
            model_name='menu',
            constraint=models.UniqueConstraint(fields=('restaurant_id', 'date'), name='same day menu'),
        ),
    ]
