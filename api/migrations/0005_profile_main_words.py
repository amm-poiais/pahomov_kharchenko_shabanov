# Generated by Django 2.0 on 2017-12-19 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20171219_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='main_words',
            field=models.ManyToManyField(related_name='main_words', to='api.Dictionary'),
        ),
    ]
