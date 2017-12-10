from django.test import TestCase
from .models import Dictionary
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ModelTestCase(TestCase):
    """This class defines the test suite for the dictionary model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.word = "Test"
        self.dictionary = Dictionary(word=self.word)
        self.dictionary.save()
        user = User.objects.create(username="nerd")
        user.portfolio.history_words.add(self.dictionary)
        user.portfolio.favorite_words.add(self.dictionary)

    def test_model_can_create_a_dictionary(self):
        """Test the dictionary model can create a dictionary."""
        old_count = Dictionary.objects.count()
        new_dictionary = Dictionary(word='Test2', description="descr")
        new_dictionary.save()
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
        self.dictionary_history = Dictionary(word='Test_history', description='description_test')
        self.dictionary_favorite = Dictionary(word='Test_favorite', description='description_test')
        self.dictionary_history.save()
        self.dictionary_favorite.save()
        user = User.objects.create(username="nerd")
        user.portfolio.favorite_words.add(self.dictionary_favorite)
        user.portfolio.history_words.add(self.dictionary_history)
        self.client.force_authenticate(user=user)

    def test_api_can_create_a_dictionary(self):
        """Test the api has dictionary creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        # res = new_client.get('/words/', kwargs={'pk': 1}, format="json")
        res = new_client.get('/words/1/', format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_api_can_get_a_dictionary(self):
    #     """Test the api can get a given dictionary."""
    #     dictionary = Dictionary.objects.get(id)
    #     response = self.client.get(
    #         '/words/',
    #         kwargs={'pk': dictionary.id}, format="json")
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertContains(response, bucketlist)

    # def test_api_can_update_dictionary(self):
    #     """Test the api can update a given dictionary."""
    #     change_dictionary = {'word': 'Test', 'description': 'New test description'}
    #     dictionary = Dictionary.objects.get(id=1)
    #     res = self.client.put(
    #         reverse('details', kwargs={'pk': dictionary.id}),
    #         change_dictionary, format='json'
    #     )
    #
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)

    # def test_api_can_delete_bucketlist(self):
    #     """Test the api can delete a dictionary."""
    #     dictionary = Dictionary.objects.get()
    #     response = self.client.delete(
    #         reverse('details', kwargs={'pk': dictionary.id}),
    #         format='json',
    #         follow=True)
    #
    #     self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
