# Generated by Django 5.1.3 on 2024-12-16 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0015_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('read', models.BooleanField(default=False)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_comment', to='CORE.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_post', to='CORE.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='CORE.user')),
            ],
        ),
    ]
