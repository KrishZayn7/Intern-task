# Generated by Django 4.1rc1 on 2022-07-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS_app', '0015_rename_intern_attendence_intern_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='TodaysDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]