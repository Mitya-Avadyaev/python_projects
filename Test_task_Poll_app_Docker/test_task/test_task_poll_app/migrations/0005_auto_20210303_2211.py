# Generated by Django 2.2.10 on 2021-03-03 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_task_poll_app', '0004_auto_20210303_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата начала'),
        ),
    ]
