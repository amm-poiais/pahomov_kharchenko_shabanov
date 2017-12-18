from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.generics import CreateAPIView

from .permissions import IsUser
from .serializers import DictionarySerializer, UserSerializer
from .models import Dictionary
from rest_framework import permissions


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsUser)

    def perform_create(self, serializer):
        """Save the post data when creating a new dictionary."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsUser)


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = User.objects.all()# <- user from reauest
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsUser)


class CreateUserView(CreateAPIView):
    model = User()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class UserCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new user."""
        serializer.save(username=self.request.user.username, password=self.request.user.password)
