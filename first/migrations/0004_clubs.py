# Generated by Django 4.1.1 on 2022-10-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_task_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clubselected', models.CharField(choices=[(1, 'IEEE'), (2, 'ACM'), (3, 'ROTARACT CLUB'), (4, 'IE'), (5, 'ISTE'), (6, 'IET')], default='IEEE', max_length=16)),
            ],
        ),
    ]
