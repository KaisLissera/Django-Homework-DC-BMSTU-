# Generated by Django 5.0.4 on 2024-04-27 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0002_alter_bugreport_project_alter_bugreport_task_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugreport',
            name='priority',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
    ]
