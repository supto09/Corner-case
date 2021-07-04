# Generated by Django 3.1.12 on 2021-07-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('EMPLOYEE', 'Employee'), ('ADMIN', 'Admin')], default='EMPLOYEE', max_length=50),
        ),
    ]
