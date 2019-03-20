from django.test import TestCase
from django.urls import reverse
from sign_up.views import CustomerFormView

class CustomerFormViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        pass
    
    def test_get_by_url(self):
        resp = self.client.get('/signup')
        self.assertEqual(resp.status_code, 200)
    
    def test_get_by_name(self):
        resp = self.client.get(reverse('signup'))
        self.assertEqual(resp.status_code, 200)