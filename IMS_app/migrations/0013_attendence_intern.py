# Generated by Django 4.1rc1 on 2022-07-20 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IMS_app', '0012_remove_attendence_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='intern',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='IMS_app.intern'),
        ),
    ]
