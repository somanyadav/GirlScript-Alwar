# Generated by Django 3.0 on 2020-05-24 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200524_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='speaker_image',
            field=models.ImageField(upload_to='speaker_image'),
        ),
        migrations.AlterField(
            model_name='userevent',
            name='cover_image',
            field=models.ImageField(upload_to='event_image'),
        ),
        migrations.AlterField(
            model_name='usereventimage',
            name='album',
            field=models.ImageField(upload_to='album_image'),
        ),
    ]
