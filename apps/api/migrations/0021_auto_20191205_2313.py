# Generated by Django 2.1.7 on 2019-12-06 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_event_certificate_hours_org'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='certificate_model',
        ),
        migrations.AddField(
            model_name='event',
            name='certificate_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.CertificateModel', verbose_name='organization certificate model'),
        ),
    ]
