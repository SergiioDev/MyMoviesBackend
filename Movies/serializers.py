from rest_framework import serializers
from Movies.models import Movies


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('movie_id', 'name')
