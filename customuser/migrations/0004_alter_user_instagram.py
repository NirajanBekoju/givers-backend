# Generated by Django 3.2.4 on 2021-06-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0003_alter_user_instagram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='instagram',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
