from unittest import TestCase
from film.models import *
from film.serializers import *
from rest_framework.test import APIClient

class TestActorAPI(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_get_actor(self):
        result = self.client.get('/actor/4/')
        self.assertEqual(result.status_code, 200)
        print(result.data)
        assert result.data['name'] == 'Sardorbek Madaminov'
        self.assertTrue(result.data['id']==4)

    def delete_actor(self):
        result = self.client.get('/actor/6/')
        self.assertEqual(result.status_code, 200)
        #self.assertEqual(result.data['id'],6)
        assert result.data['id'] == 6


