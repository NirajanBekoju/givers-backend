# Generated by Django 3.2.5 on 2022-06-24 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20220624_0750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likeevent',
            old_name='event',
            new_name='events',
        ),
    ]