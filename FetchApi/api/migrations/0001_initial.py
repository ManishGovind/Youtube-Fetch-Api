# Generated by Django 4.0.6 on 2022-07-12 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YTVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=500)),
                ('published_at', models.DateTimeField()),
                ('thumbnail_url', models.CharField(max_length=300)),
                ('channel_id', models.CharField(max_length=100)),
            ],
        ),
    ]
