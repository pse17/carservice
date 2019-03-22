'''Our models'''
from django.db import models

class Engeneer(models.Model):
    """Model representing a car service engineer"""
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Customer(models.Model):
    '''Model representing a customer'''
    name = models.CharField(max_length=120, verbose_name='Full name')
    car = models.CharField(max_length=120, verbose_name='Make and model of car')
    engeneer = models.ForeignKey(Engeneer, on_delete=models.SET_NULL, null=True)
    signup_date = models.DateField(verbose_name='Sign up time')
    signup_time = models.CharField(max_length=5)

    def __str__(self):
        '''String for representing the Customer object.'''
        return 'Владелец %s автомобиль %s записан к мастеру %s на %s в %s' % (
            self.name, self.car, self.engeneer.name, self.signup_date, self.signup_time
            )


class SignUpRange(models.Model):
    '''Model representing time ranges'''
    signup_time = models.CharField(max_length=5)

    def __str__(self):
        return self.signup_time
