# Generated by Django 4.1rc1 on 2022-07-20 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS_app', '0005_alter_supervisor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intern',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]