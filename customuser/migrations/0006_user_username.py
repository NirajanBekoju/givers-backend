# Generated by Django 3.2.4 on 2021-06-29 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0005_user_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
