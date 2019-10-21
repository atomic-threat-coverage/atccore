# Generated by Django 2.2.4 on 2019-09-01 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loggingpolicy',
            name='event_id',
        ),
        migrations.AddField(
            model_name='loggingpolicy',
            name='event_id',
            field=models.ManyToManyField(null=True, to='atc.EventID', verbose_name='Event ID(s)'),
        ),
        migrations.RemoveField(
            model_name='loggingpolicy',
            name='reference',
        ),
        migrations.AddField(
            model_name='loggingpolicy',
            name='reference',
            field=models.ManyToManyField(blank=True, null=True, to='atc.Reference', verbose_name='Reference(s)'),
        ),
    ]