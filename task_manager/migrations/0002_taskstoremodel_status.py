# Generated by Django 4.2.3 on 2023-08-11 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskstoremodel',
            name='status',
            field=models.CharField(choices=[('Incomplete', 'Incomplete'), ('Complete', 'Complete')], default='Incomplete', max_length=30),
        ),
    ]