from django.test import TestCase
from django.urls import reverse
from sign_up.views import CustomerFormView, EngeneerFormView

class CustomerFormViewTest(TestCase):
    ''' '''
    @classmethod
    def setUpTestData(cls):
        pass

    def test_get_by_url(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_get_by_name(self):
        resp = self.client.get(reverse('customer'))
        self.assertEqual(resp.status_code, 200)

class EngeneerFormViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def test_get_by_name(self):
        resp = self.client.get(reverse('engeneer'))
        self.assertEqual(resp.status_code, 200)

