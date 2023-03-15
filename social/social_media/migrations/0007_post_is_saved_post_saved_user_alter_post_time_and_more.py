# Generated by Django 4.1.4 on 2023-03-14 11:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social_media', '0006_alter_post_date_alter_post_time_saved'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_saved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='saved_user',
            field=models.ManyToManyField(blank=True, related_name='saved_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(blank=True, default='04:35:08'),
        ),
        migrations.DeleteModel(
            name='saved',
        ),
    ]