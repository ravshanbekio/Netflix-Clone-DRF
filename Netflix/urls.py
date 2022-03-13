"""Netflix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from film.views import (ActorAPIView, CommentViewSet, Hello, 
                        ActorAPIView, MovieView, UserAPIView,
                        UserViewSet, MovieViewSet, ActorViewSet)
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Netflix API",
      default_version='v1',
      description="Netflix dasturining klon versiyasi. Bemalol kirib ishlatishingiz mumkin. API bepul!!! \n Istaganingizcha foydalaning",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact("Ravshanbek Madaminov <ravshanbekmadaminov68@gmail.com> <+998903036415>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



r = DefaultRouter()
r.register('comment',CommentViewSet)
r.register('user',UserViewSet)
r.register('movies', MovieViewSet)
r.register('actor',ActorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello',Hello.as_view()),
    path('actors/',ActorAPIView.as_view()),
    path('actors/<int:pk>/',ActorAPIView.as_view()),
    path('movie/',MovieView.as_view()),
    path('movie/<int:pk>/',MovieView.as_view()),
    path('users/',UserAPIView.as_view()),
    path('users/<int:pk>/',UserAPIView.as_view()),
    path('',include(r.urls)),
    path('doc/swagger',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc/',schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
]
