# Generated by Django 3.1.1 on 2022-02-18 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('artist', 'Artist'), ('listener', 'Listener')], default='listener', max_length=10, null=True)),
                ('bio', models.TextField(null=True)),
                ('photo', models.ImageField(null=True, upload_to='Profile-Picture')),
                ('website', models.URLField(null=True)),
                ('face_book', models.URLField(null=True)),
                ('twitter', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserFollowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('following_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='users.profile')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='users.profile')),
            ],
        ),
    ]
