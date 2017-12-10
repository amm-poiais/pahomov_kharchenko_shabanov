from rest_framework import generics
from .serializers import DictionarySerializer
from .models import Dictionary


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new dictionary."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
