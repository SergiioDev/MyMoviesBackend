from djongo import models
from django.utils import timezone

from Movies.models import Movie, MovieForm
from Users.models import User


class WatchList(models.Model):
    watchlist_name = models.CharField(max_length=100)
    date_created = models.DateField(default=timezone.now)
    movies = models.ArrayField(
        model_container=Movie,
        model_form_class=MovieForm
    )


class WatchLists(models.Model):
    user = models.EmbeddedField(
        model_container=User
    )
    watchlists = models.ArrayField(
        model_container=WatchList,
    )
    watchlists_count = watchlists.auto_creation_counter()

    objects = models.DjongoManager()
