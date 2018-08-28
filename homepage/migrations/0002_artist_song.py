# Generated by Django 2.0.2 on 2018-08-15 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=500)),
                ('artist_image', models.CharField(max_length=1000)),
                ('artist_desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=500)),
                ('song_path', models.CharField(max_length=1000)),
                ('song_length', models.CharField(max_length=100)),
                ('song_lyrics', models.CharField(max_length=10000)),
                ('song_image', models.CharField(max_length=1000)),
                ('song_album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Album')),
                ('song_artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Artist')),
            ],
        ),
    ]