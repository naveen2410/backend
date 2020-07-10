# Generated by Django 3.0.7 on 2020-07-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qaconfig', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qaconfig',
            name='password',
        ),
        migrations.RemoveField(
            model_name='qaconfig',
            name='systemendpoint',
        ),
        migrations.RemoveField(
            model_name='qaconfig',
            name='systemname',
        ),
        migrations.RemoveField(
            model_name='qaconfig',
            name='user',
        ),
        migrations.AddField(
            model_name='qaconfig',
            name='adminpass',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='qaconfig',
            name='adminuser',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='qaconfig',
            name='client',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='qaconfig',
            name='githuburl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='qaconfig',
            name='ipaddress',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='qaconfig',
            name='port',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='qaconfig',
            name='qaconnid',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='qaconfig',
            name='sysid',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='qaconfig',
            name='systemtype',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qaconfig',
            name='triggerrate',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='qaconfig',
            name='triggeruom',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
