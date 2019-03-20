from django import forms
from sign_up.models import Customer, Engeneer, SignUpRange

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=120)
    car = forms.CharField(max_length=120)
    engeneer = forms.ModelChoiceField(queryset=Engeneer.objects.all())
    signup_date = forms.DateField(localize=True)

    '''
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList, label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None):
        super(CustomerForm,self).__init__(data=data, files=files, auto_id=auto_id, prefix=prefix, initial=initial, error_class=error_class, label_suffix=label_suffix, empty_permitted=empty_permitted, field_order=field_order, use_required_attribute=use_required_attribute, renderer=renderer)
        ranges = SignUpRange.objects.all()
        for _, name in ranges:
            self.fields[name] = forms.BooleanField(initial=False)
    '''
    def __init__(self, *args, **kwargs ):
        super(CustomerForm,self).__init__(*args, **kwargs)
        ranges = SignUpRange.objects.values('signup_time') # Return the list of dicts. Only signup_time field.
        for time_range in ranges:
            self.fields[time_range['signup_time']] = forms.BooleanField(initial=False)
