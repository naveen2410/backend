# Generated by Django 3.0.7 on 2020-07-10 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0003_auto_20200703_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
