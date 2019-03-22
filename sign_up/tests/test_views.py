''' Test our views'''
from datetime import date
from django.test import TestCase
from django.urls import reverse
from sign_up.views import CustomerFormView, EngeneerFormView
from sign_up.models import Customer, Engeneer, SignUpRange

class CustomerFormViewTest(TestCase):
    ''' Test CustomerFormView'''
    @classmethod
    def setUpTestData(cls):
        engeneer = Engeneer(name='мастер по двигателям')
        engeneer.save()
        Customer.objects.create(
            name='Николай Фоменко',
            car='Kia Rio',
            engeneer = engeneer,
            signup_time='10:00',
            signup_date=date.today()
        )

    def test_get_by_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_get_by_name(self):
        response = self.client.get(reverse('customer', kwargs={'eng_id': 1, 'signup_date': date.today()}))
        self.assertEqual(response.status_code, 200)
    
    def test_get_context_data(self):
        #Get queryset with test data (without signup_time='10:00')
        occupied_range = Customer.objects.values('signup_time').all()
        occupied_range = occupied_range.filter(engeneer_id=1)
        occupied_range = occupied_range.filter(signup_date=date.today())
        queryset = SignUpRange.objects.exclude(signup_time__in=occupied_range).all()

        #Get context
        response = self.client.get(reverse('customer', kwargs={'eng_id': 1, 'signup_date': date.today()}))
        #It`s impossible to compare django queryset objects
        #Convert to list
        self.assertEqual(list(response.context['form'].fields['ranges'].queryset), list(queryset))
         

class EngeneerFormViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def test_get_by_name(self):
        response = self.client.get(reverse('engeneer'))
        self.assertEqual(response.status_code, 200)

