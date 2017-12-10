from rest_framework import serializers
from .models import Dictionary


class DictionarySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Dictionary
        fields = ('id', 'word', 'description')