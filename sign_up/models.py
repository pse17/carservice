from django.db import models

class Engeneer(models.Model):
    name = models.CharField(max_length=60) 

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=120, verbose_name='Full name')
    car = models.CharField(max_length=120, verbose_name='Make and model of car')
    engeneer = models.ForeignKey(Engeneer, on_delete=models.SET_NULL, null=True)
    signup_date = models.DateField(verbose_name='Sign up time')
    signup_time = models.CharField(max_length=5)


class SignUpRange(models.Model):
    signup_time = models.CharField(max_length=5)

    def __str__(self):
        return self.signup_time