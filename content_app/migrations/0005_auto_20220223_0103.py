# Generated by Django 3.1.1 on 2022-02-22 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0004_auto_20220219_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_type',
            field=models.CharField(choices=[('song', 'Song'), ('mixtape', 'Mixtape')], default='song', max_length=10),
        ),
    ]