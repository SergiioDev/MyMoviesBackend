from django.core.files.storage import FileSystemStorage
from djongo import models
from django import forms
from django.contrib.postgres.fields import ArrayField
class Movie(models.Model):
    id = models.AutoField(primary_key=True,default=1)
    title = models.CharField(max_length=500)
    poster = models.ImageField(upload_to='images/poster')
    header = models.ImageField(upload_to='images/header')
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
