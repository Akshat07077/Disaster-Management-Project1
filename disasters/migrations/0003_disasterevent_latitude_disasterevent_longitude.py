# Generated by Django 4.2.11 on 2024-06-20 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disasters', '0002_alter_disasterevent_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='disasterevent',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='disasterevent',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
