# Generated by Django 3.1.1 on 2022-02-18 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0003_auto_20220216_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='song',
            name='slug',
        ),
    ]
