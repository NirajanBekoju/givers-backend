# Generated by Django 3.2.4 on 2021-06-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_events_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='banner',
            field=models.ImageField(default='avatar.jpg', upload_to='Banner_Images'),
        ),
    ]
