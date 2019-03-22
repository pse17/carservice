''' Tests our models '''
from datetime import date
from django.test import TestCase
from sign_up.models import Engeneer, Customer, SignUpRange

class EngeneerModelTest(TestCase):
    ''' Tests Engeneer model'''

    @classmethod
    def setUpTestData(cls):
        Engeneer.objects.create(name='мастер по двигателям')

    def test_name_max_length(self):
        engeneer = Engeneer.objects.get(id=1)
        max_length = engeneer._meta.get_field('name').max_length
        self.assertEqual(max_length, 60)
    
    def test_representing_engeneer_object(self):
        engeneer = Engeneer.objects.get(id=1)
        self.assertEqual(str(engeneer), 'мастер по двигателям')

class CustomerModelTest(TestCase):
    ''' Test customer model'''

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

    def test_signup_time_max_lenght(self):
        customer = Customer.objects.get(id=1)
        #Must be the same
        max_length = customer._meta.get_field('signup_time').max_length
        self.assertEqual(max_length, 5)
    
    def test_representing_customer_object(self):
        customer = Customer.objects.get(id=1)
        string_for_representing = 'Владелец %s автомобиль %s записан к мастеру %s на %s в %s' % (
            'Николай Фоменко',
            'Kia Rio',
            'мастер по двигателям',
            date.today(),
            '10:00'
            )
        self.assertEqual(str(customer), string_for_representing)

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
    
    def test_representing_sign_up_range_object(self):
        signup_range = SignUpRange.objects.get(id=1)
        self.assertEqual(str(signup_range), '10:00')
