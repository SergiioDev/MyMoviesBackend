from djongo import models
from django.conf import settings
from djongo.storage import GridFSStorage

grid_fs_storage = GridFSStorage(collection='images', base_url=''.join([settings.BASE_URL, 'images/']))


class Movie(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=500)
    poster = models.ImageField(upload_to='movies', storage=grid_fs_storage)
    header = models.ImageField(upload_to='movies', storage=grid_fs_storage)
    release_date = models.DateField()
    average_rating = models.IntegerField(default=0)
    user_rating = models.IntegerField(default=0)
    genres = models.CharField(max_length=200)
    is_adult = models.BooleanField(default=False)

    objects = models.DjongoManager()
