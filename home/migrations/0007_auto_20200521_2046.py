# Generated by Django 3.0 on 2020-05-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200520_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='github_account',
            field=models.URLField(max_length=100),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='linkedin_account',
            field=models.URLField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='current_status',
            field=models.CharField(choices=[('0', 'NO'), ('1', 'YES')], default='1', max_length=4),
        ),
        migrations.AlterField(
            model_name='team',
            name='github_url',
            field=models.URLField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin_url',
            field=models.URLField(max_length=100),
        ),
    ]
