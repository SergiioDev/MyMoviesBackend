from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Movies.models import Movie
from Movies.serializers import MovieSerializer
