# Generated by Django 3.2 on 2021-04-24 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0003_auto_20210424_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='changed_by_admin',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=0),
        ),
    ]
