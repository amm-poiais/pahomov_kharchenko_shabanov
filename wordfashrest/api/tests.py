from django.test import TestCase
from .models import Dictionary
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


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

    def test_api_can_get_a_dictionary(self):
        """Test the api can get a given dictionary."""
        dictionary = Dictionary.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': dictionary.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, dictionary)

    def test_api_can_update_dictionary(self):
        """Test the api can update a given dictionary."""
        change_dictionary = {'word': 'Test', 'description': 'New test description'}
        dictionary = Dictionary.objects.get(id=1)
        res = self.client.put(
            reverse('details', kwargs={'pk': dictionary.id}),
            change_dictionary, format='json'
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a dictionary."""
        dictionary = Dictionary.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': dictionary.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
