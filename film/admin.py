from re import A
from django.contrib import admin
from .models import Actor, Movie, Users, Comment

admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Users)
admin.site.register(Comment)

