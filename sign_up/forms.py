from django import forms
from sign_up.models import Customer, Engeneer, SignUpRange

class EngeneerForm(forms.Form):
    engeneer = forms.ModelChoiceField(queryset=Engeneer.objects.all())
    signup_date = forms.DateField()

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=120)
    car = forms.CharField(max_length=120)
    ranges = forms.ModelChoiceField(queryset=SignUpRange.objects.all())
'''
class CustomerForm(forms.Form):
    name = forms.CharField(max_length=120)
    car = forms.CharField(max_length=120)
    engeneer = forms.ModelChoiceField(queryset=Engeneer.objects.all())
    signup_date = forms.DateField(localize=True)

    def __init__(self, *args, **kwargs ):
        super(CustomerForm,self).__init__(*args, **kwargs)
        ranges = SignUpRange.objects.values('signup_time') # Return the list of dicts. Only signup_time field.
        for time_range in ranges:
            self.fields[time_range['signup_time']] = forms.BooleanField(initial=False)
'''