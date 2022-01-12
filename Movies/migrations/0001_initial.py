# Generated by Django 3.1.12 on 2022-01-12 12:07

from django.db import migrations, models
import djongo.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('poster', models.ImageField(storage=djongo.storage.GridFSStorage(base_url='myfilesmovies/images/', collection='moviesImages'), upload_to='movies')),
                ('header', models.ImageField(storage=djongo.storage.GridFSStorage(base_url='myfilesmovies/images/', collection='moviesImages'), upload_to='movies')),
                ('release_date', models.DateField()),
                ('average_rating', models.IntegerField(default=0)),
                ('user_rating', models.IntegerField(default=0)),
                ('is_adult', models.BooleanField(default=False)),
            ],
        ),
    ]
