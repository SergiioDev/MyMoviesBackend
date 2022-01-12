# Generated by Django 3.1.12 on 2022-01-12 12:15

from django.db import migrations, models
import djongo.storage


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='header',
            field=models.ImageField(storage=djongo.storage.GridFSStorage(base_url='imagesimages/', collection='images'), upload_to='movies'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(storage=djongo.storage.GridFSStorage(base_url='imagesimages/', collection='images'), upload_to='movies'),
        ),
    ]