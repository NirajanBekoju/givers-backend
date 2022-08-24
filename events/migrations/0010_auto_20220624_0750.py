# Generated by Django 3.2.5 on 2022-06-24 02:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0009_likeevents'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LikeEvents',
            new_name='LikeEvent',
        ),
        migrations.RenameField(
            model_name='likeevent',
            old_name='events',
            new_name='event',
        ),
    ]
