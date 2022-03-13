from unittest import TestCase
from film.models import *
from film.serializers import *

class TestMovieSerializer(TestCase):
    def test_all(self):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        assert serializer.data[0]['title'] == 'Avengers'
        self.assertIsNotNone(serializer.data[0]['id'])