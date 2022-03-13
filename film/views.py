from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Actor
from .serializers import *
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

class Hello(APIView):
    def get(self, request):
        malumot = {'xabar':"Salom dunyo"}
        return Response(malumot)

    def post(self, request):
        data = {'message':"Ma'lumot qabul qilindi!"}
        return Response(data)

class ActorAPIView(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer_class = ActorSerializer(actors, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        serializer_class = ActorSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        a = Actor.objects.get(id=pk)
        ser = ActorSerializer(a, request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        actors = Actor.objects.get(id=pk)
        serializer_class = ActorSerializer(actors, data=request.data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        actor = Actor.objects.get(pk=pk)
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MovieView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer_class = MovieSerializer(movies, many=True)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = MovieSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        movies = Movie.objects.get(id=pk)
        serializer_class = MovieSerializer(movies, request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        movies = Movie.objects.get(id=pk)
        serializer_class = MovieSerializer(movies, data=request.data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        movie = Movie.objects.get(id=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, request, pk):
        users = Users.objects.get(id=pk)
        serializer_class = UserSerializer(users)
        return Response(serializer_class.data)
    def post(self, request):
        serializer_class = UserSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        user = Users.objects.get(id=pk)
        serializer_class = UserSerializer(user, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        user = Users.objects.get(id=pk)
        serializer_class = UserSerializer(user, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        user = Users.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=["GET", "POST"])
    def aktor(self, request, pk):
        movie = Movie.objects.get(id=pk)
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            a = Actor.objects.last()
            movie.actors.add(a)
            movie.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer