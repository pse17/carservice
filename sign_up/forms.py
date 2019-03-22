''' Our forms'''
from django import forms
from sign_up.models import Engeneer, SignUpRange

class EngeneerForm(forms.Form):
    '''Form for the selection of the engineer and the date'''
    engeneer = forms.ModelChoiceField(queryset=Engeneer.objects.all())
    signup_date = forms.DateField()

class CustomerForm(forms.Form):
    '''Form for the selection time range'''
    name = forms.CharField(max_length=120)
    car = forms.CharField(max_length=120)
    ranges = forms.ModelChoiceField(queryset=SignUpRange.objects.all())
