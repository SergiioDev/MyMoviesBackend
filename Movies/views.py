from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Movies.models import Movies
from Movies.serializers import MovieSerializer


class MovieCreate(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format='json'):
        movies = Movies.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
        

    def post(self, request, format='json'):
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            movie = MovieSerializer.save()
            return Response({'message': 'created successfully'}, status=status.HTTP_201_CREATED)

        return Response({'message': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

