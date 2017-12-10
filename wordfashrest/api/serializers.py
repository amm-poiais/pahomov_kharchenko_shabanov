from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Dictionary


class DictionarySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Dictionary
        fields = ('id', 'word', 'description')


class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    #history_words = DictionarySerializer(source="profile.history_words", many=True)
    #favorite_words = DictionarySerializer(source="profile.favorite_words", many=True)
    history_words = DictionarySerializer(source="profile.history_words", many=True, allow_null=True, read_only=True)
    favorite_words = DictionarySerializer(source="profile.favorite_words", many=True, allow_null=True,  read_only=True)

    class Meta:
        """Map this serializer to a model and their fields."""
        model = User
        fields = ('id', 'username', 'password', 'history_words', 'favorite_words')
