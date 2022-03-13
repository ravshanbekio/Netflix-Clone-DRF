from unittest import TestCase
from film.models import Actor, Movie, Users, Comment

class TestActor(TestCase):
    def test_movie(self):
        movies = Movie.objects.all()
        #self.assertIsNotNone(movies[0].imdb)

class TestUser(TestCase):
    def test_user(self):
        pass
