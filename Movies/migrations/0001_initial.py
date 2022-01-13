# Generated by Django 3.0.5 on 2022-01-13 10:59

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
                ('poster', models.ImageField(storage=djongo.storage.GridFSStorage(base_url='imagesimages/', collection='images'), upload_to='movies')),
                ('header', models.ImageField(storage=djongo.storage.GridFSStorage(base_url='imagesimages/', collection='images'), upload_to='movies')),
                ('release_date', models.DateField()),
                ('average_rating', models.IntegerField(default=0)),
                ('user_rating', models.IntegerField(default=0)),
                ('genres', models.CharField(max_length=200)),
                ('is_adult', models.BooleanField(default=False)),
            ],
        ),
    ]
