# Generated by Django 3.0.7 on 2020-07-04 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qaconfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systemname', models.CharField(max_length=10)),
                ('systemendpoint', models.CharField(max_length=10)),
                ('user', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
