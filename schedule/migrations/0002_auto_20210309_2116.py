# Generated by Django 3.0.8 on 2021-03-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='remind_minutes',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='triage',
            field=models.SmallIntegerField(),
        ),
    ]