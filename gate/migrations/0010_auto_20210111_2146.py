# Generated by Django 3.0.8 on 2021-01-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gate', '0009_auto_20210111_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='token',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
