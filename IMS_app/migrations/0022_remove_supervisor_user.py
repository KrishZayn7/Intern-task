# Generated by Django 4.1rc1 on 2022-07-21 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IMS_app', '0021_supervisor_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervisor',
            name='user',
        ),
    ]
