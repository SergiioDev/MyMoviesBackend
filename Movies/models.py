from djongo import models
from django import forms

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    poster = models.ImageField(upload_to='images/' + str(movie_id) + 'poster/')
    header = models.ImageField(upload_to='images/' + str(movie_id) + 'header/')
    release_date = models.DateField()
    average_rating = models.IntegerField(default=0)
    user_rating = models.IntegerField(default=0)
    genres = models.ArrayReferenceField(to=Genre, on_delete=models.CASCADE)
    is_adult = models.BooleanField(default=False)

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = (
            'movie_id', 'title', 'poster', 'header', 'release_date', 'average_rating', 'user_rating', 'genres',
            'is_adult'
        )
