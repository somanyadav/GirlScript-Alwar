# Generated by Django 3.0 on 2020-05-18 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200518_2033'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Speakers',
            new_name='Speaker',
        ),
        migrations.RenameModel(
            old_name='UserEvents',
            new_name='UserEvent',
        ),
        migrations.RenameModel(
            old_name='UserEventImages',
            new_name='UserEventImage',
        ),
    ]
