# Generated by Django 3.0 on 2020-05-18 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speakers',
            name='speaker_image',
            field=models.ImageField(default='speaker_image/default.jpg', upload_to='speaker_image'),
        ),
        migrations.AddField(
            model_name='team',
            name='user_image',
            field=models.ImageField(default='profile_image/default.jpg', upload_to='profile_image'),
        ),
        migrations.AddField(
            model_name='telegramgroup',
            name='group_name',
            field=models.TextField(default='NULL', max_length=200),
        ),
        migrations.AddField(
            model_name='userevents',
            name='cover_image',
            field=models.ImageField(default='event_image/default.jpg', upload_to='event_image'),
        ),
        migrations.AddField(
            model_name='whattsappgroup',
            name='group_name',
            field=models.TextField(default='NULL', max_length=200),
        ),
        migrations.CreateModel(
            name='UserEventImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ImageField(default='album_image/default.jpg', upload_to='album_image')),
                ('event_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.UserEvents')),
            ],
        ),
    ]
