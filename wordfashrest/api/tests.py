from django.test import TestCase
from .models import Dictionary
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class ModelTestCase(TestCase):
    """This class defines the test suite for the dictionary model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.word = "Test"
        self.dictionary = Dictionary(word=self.word)

    def test_model_can_create_a_dictionary(self):
        """Test the dictionary model can create a dictionary."""
        old_count = Dictionary.objects.count()
        self.dictionary.save()
        new_count = Dictionary.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.dictionary_data = {'word': 'Test', 'description': 'Test description'}
        self.response = self.client.post(
            reverse('create'),
            self.dictionary_data,
            format="json")

    def test_api_can_create_a_dictionary(self):
        """Test the api has dictionary creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)