# Generated by Django 3.1.4 on 2020-12-06 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='id',
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
