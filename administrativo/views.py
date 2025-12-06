from django.shortcuts import render
from rest_framework import viewsets

from .models import Rol,User
from .serializers import RolSerializer, UserSerializer


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

