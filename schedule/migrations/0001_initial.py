# Generated by Django 3.0.8 on 2021-02-17 12:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re
import unixtimestampfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gate', '0002_auto_20210217_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid'), django.core.validators.MaxLengthValidator(64)])),
                ('detail', models.TextField(blank=True, null=True)),
                ('triage', models.SmallIntegerField(choices=[(4, 'black'), (3, 'green'), (2, 'orange'), (1, 'red')], default=4)),
                ('do_remind', models.BooleanField(default=False)),
                ('remind_minutes', models.SmallIntegerField(choices=[(0, 'No remind'), (10, '10 minutes'), (15, '15 minutes'), (30, '30 minutes'), (45, '45 minutes'), (60, '60 minutes')], default=0)),
                ('from_time', unixtimestampfield.fields.UnixTimeStampField()),
                ('to_time', unixtimestampfield.fields.UnixTimeStampField()),
                ('updated_time', unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True)),
                ('created_time', unixtimestampfield.fields.UnixTimeStampField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calendar_user_id', to='gate.User')),
            ],
            options={
                'verbose_name': 'user calendar table',
                'verbose_name_plural': 'user calendar table',
                'ordering': ['from_time'],
            },
        ),
    ]
