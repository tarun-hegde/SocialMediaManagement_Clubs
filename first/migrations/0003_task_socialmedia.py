# Generated by Django 4.1.1 on 2022-10-07 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_alter_task_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='socialmedia',
            field=models.CharField(choices=[('I', 'Instagram'), ('W', 'Whatsapp'), ('L', 'LinkedIn')], default='LinkedIn', max_length=9),
        ),
    ]