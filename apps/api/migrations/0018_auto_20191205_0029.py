# Generated by Django 2.1.7 on 2019-12-05 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20190320_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificatemodel',
            name='text',
            field=models.TextField(help_text='Available variables: {name}, {event}, {cpf}, {event_date}, {event_place}, {event_duration}, {event_min_percent}.', verbose_name='text'),
        ),
    ]
