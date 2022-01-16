from djongo import models
from django.utils import timezone
from Movies.models import Movie
from Users.models import User
from django import forms


class WatchList(models.Model):
    watchlist_name = models.CharField(max_length=100)
    date_created = models.DateField(default=timezone.now)
    movies = models.ArrayReferenceField(
        to=Movie, on_delete=models.CASCADE
    )


class WatchListForm(forms.ModelForm):
    class Meta:
        model = WatchList
        fields = (
            'watchlist_name', 'date_created', 'movies'
        )


class WatchLists(models.Model):
    user = models.ArrayReferenceField(
        to=User, on_delete=models.CASCADE
    )
    watchlists = models.ArrayReferenceField(
        to=WatchList, on_delete=models.CASCADE
    )
    watchlists_count = models.IntegerField(default=0)

    objects = models.DjongoManager()
