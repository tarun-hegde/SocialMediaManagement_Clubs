# Generated by Django 4.1.1 on 2022-10-08 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_alter_clubs_clubselected'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTasks',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first.task')),
                ('status', models.BooleanField(default=False)),
            ],
            bases=('first.task',),
        ),
    ]
