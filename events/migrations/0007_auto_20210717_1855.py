# Generated by Django 3.2.4 on 2021-07-17 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_events_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='toggle',
        ),
        migrations.AddField(
            model_name='events',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
