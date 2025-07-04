# Generated by Django 5.1.3 on 2024-12-19 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0018_notifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='CORE.post'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='CORE.user'),
        ),
        migrations.CreateModel(
            name='CoverPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverphoto', models.ImageField(blank=True, null=True, upload_to='cover_pictures/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CORE.user')),
            ],
        ),
    ]
