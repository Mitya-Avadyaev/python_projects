# Generated by Django 2.2.10 on 2021-03-03 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_task_poll_app', '0005_auto_20210303_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pos_answers',
            field=models.ManyToManyField(blank=True, null=True, to='test_task_poll_app.Answer', verbose_name='Ответы'),
        ),
    ]
