from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.
class ConversionLogicTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response = self.client.get(
            reverse()
        )  # reverse("named-url", kwargs={}, args=[])
