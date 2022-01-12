from django.core.files.storage import FileSystemStorage
from djongo import models
from django.conf import settings
from djongo.storage import GridFSStorage
from django import forms
from django.contrib.postgres.fields import ArrayField

grid_fs_storage = GridFSStorage(collection='images', base_url=''.join([settings.BASE_URL, 'images/']))
class Movie(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=500)
    poster = models.ImageField(upload_to='movies', storage=grid_fs_storage)
    header = models.ImageField(upload_to='movies', storage=grid_fs_storage)
    release_date = models.DateField()
    average_rating = models.IntegerField(default=0)
    user_rating = models.IntegerField(default=0)
    #genres = ArrayField(models.CharField(max_length=20))
    is_adult = models.BooleanField(default=False)


#Note: Investigate if we need this
#class MovieForm(forms.ModelForm):
#   class Meta:
#        model = Movie
#        fields = (
#            'movie_id', 'title', 'poster', 'header', 'release_date', 'average_rating', 'user_rating', 'genres',
#            'is_adult'
#        )
