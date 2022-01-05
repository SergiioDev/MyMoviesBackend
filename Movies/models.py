from django.db import models


class Movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
