from django.test import TestCase
from .models import Dictionary


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

