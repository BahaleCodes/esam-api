# Generated by Django 3.1.1 on 2022-03-05 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0007_remove_album_song_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.CreateModel(
            name='Album_Song',
            fields=[
                ('song_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content_app.song')),
                ('album', models.ForeignKey(default=b'N', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='album', to='content_app.album')),
            ],
            bases=('content_app.song',),
        ),
    ]
