from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .serializers import UserSerializer, TicketSerializer, CategorySerializer

from django.contrib.auth.models import User
from .models import Ticket, Category

# ViewSets define the view behavior
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
