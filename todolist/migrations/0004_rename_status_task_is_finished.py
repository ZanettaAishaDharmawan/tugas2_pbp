# Generated by Django 4.1.1 on 2022-09-27 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_alter_task_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='status',
            new_name='is_finished',
        ),
    ]
