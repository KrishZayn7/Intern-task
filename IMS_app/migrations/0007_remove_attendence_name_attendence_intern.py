# Generated by Django 4.1rc1 on 2022-07-20 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IMS_app', '0006_alter_intern_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendence',
            name='name',
        ),
        migrations.AddField(
            model_name='attendence',
            name='intern',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='IMS_app.intern'),
        ),
    ]