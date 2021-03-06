# Generated by Django 2.0 on 2017-12-18 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('word', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=1023)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_words', models.ManyToManyField(related_name='favorite_words', to='api.Dictionary')),
                ('history_words', models.ManyToManyField(related_name='history_words', to='api.Dictionary')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
