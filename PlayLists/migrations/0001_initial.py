# Generated by Django 3.0.5 on 2022-01-16 11:37

import Movies.models
import PlayLists.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('watchlist_name', models.CharField(max_length=100)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('movies', djongo.models.fields.EmbeddedField(model_container=Movies.models.Movie)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WatchLists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watchlists', djongo.models.fields.EmbeddedField(model_container=PlayLists.models.WatchList, model_form_class=PlayLists.models.WatchListForm)),
                ('watchlists_count', models.IntegerField(default=0)),
                ('user', djongo.models.fields.ArrayReferenceField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
