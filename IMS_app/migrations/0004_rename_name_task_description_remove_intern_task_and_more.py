# Generated by Django 4.1rc1 on 2022-07-20 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS_app', '0003_attendence_status_intern_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='intern',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='allot_to',
            field=models.ManyToManyField(to='IMS_app.intern'),
        ),
        migrations.AddField(
            model_name='task',
            name='alloted_by',
            field=models.ManyToManyField(to='IMS_app.supervisor'),
        ),
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
