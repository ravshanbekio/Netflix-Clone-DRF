from rest_framework.serializers import ModelSerializer
from .models import Actor, Movie, Comment, Users
from rest_framework.exceptions import APIException

class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = ('__all__')
    
    def validate_name(self, value):
        if len(value) < 5:
            raise APIException("Ism juda qisqa")
        return value    

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')

    def validate_imdb(self, value):
        if value < 3:
            raise APIException("Reyting juda past!")
        return value

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def validate_text(self, value):
        if len(value) < 3:
            raise APIException("Komment juda qisqa!")
        return value

class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'