''' Tests our models '''
from datetime import date
from django.test import TestCase
from sign_up.models import Engeneer, Customer, SignUpRange

class EngeneerModelTest(TestCase):
    ''' Tests Engeneer model'''

    @classmethod
    def setUpTestData(cls):
        Engeneer.objects.create(name="Tyre master")

    def test_name_max_length(self):
        engeneer = Engeneer.objects.get(id=1)
        max_length = engeneer._meta.get_field('name').max_length
        self.assertEqual(max_length, 60)

class CustomerModelTest(TestCase):
    ''' Test customer model'''

    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(name='John Doe', signup_time='10:00', signup_date=date.today())
    
    def test_signup_time_max_lenght(self):
        customer = Customer.objects.get(id=1)
        #Must be the same
        max_length = customer._meta.get_field('signup_time').max_length
        self.assertEqual(max_length, 5)

class SignUpRangeModelTest(TestCase):
    ''' Test SignUpRange model'''

    @classmethod
    def setUpTestData(cls):
        SignUpRange.objects.create(signup_time='10:00')
    
    def test_signup_time_max_lenght(self):
        signup_range = SignUpRange.objects.get(id=1)
        #Must be the same
        max_length = signup_range._meta.get_field('signup_time').max_length
        self.assertEqual(max_length, 5)