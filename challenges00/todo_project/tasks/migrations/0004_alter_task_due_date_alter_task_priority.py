# Generated by Django 5.1 on 2024-09-02 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_due_date_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('low', 'Faible'), ('medium', 'Moyenne'), ('high', 'Élevée')], default='medium', max_length=10),
        ),
    ]
