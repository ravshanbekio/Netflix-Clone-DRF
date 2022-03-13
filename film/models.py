from django.db import models
from django.contrib.auth.models import User

class Actor(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    gender = models.CharField(max_length=6, choices=[("Ayol","Ayol"),("Erkak","Erkak")])
    nation = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    yonalish = models.CharField(max_length=15)
    actors = models.ManyToManyField(Actor, related_name='aktyorni_kinolari')
    imdb = models.FloatField()

    def __str__(self):
        return self.title
class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

class Comment(models.Model):
    text = models.CharField(max_length=400)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='user_commentlari')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text