# Generated by Django 5.1.4 on 2024-12-09 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0005_delete_postprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='no_like',
            field=models.IntegerField(default=0),
        ),
    ]
