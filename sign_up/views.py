''' Django views is here'''
from django.views.generic import FormView
from django.urls import reverse_lazy
from sign_up.forms import CustomerForm, EngeneerForm
from sign_up.models import Customer, SignUpRange, Engeneer

class EngeneerFormView(FormView):
    '''Generic class based view selection of the engineer and the date'''
    template_name = 'engeneer.html'
    form_class = EngeneerForm

    def form_valid(self, form):
        self.success_url = '/signup/%s/%s' % (form.data['engeneer'], form.data['signup_date'])
        return super().form_valid(form)

class CustomerFormView(FormView):
    '''Generic class based view selection time range'''
    template_name = 'customer.html'
    form_class = CustomerForm
    success_url = reverse_lazy('engeneer')

    def get_context_data(self, **kwargs):
        signup_date = self.kwargs['signup_date']
        engeneer_id = self.kwargs['eng_id']

        context = super(CustomerFormView, self).get_context_data(**kwargs)
        context['signup_date'] = signup_date

        #Get the occupied time ranges
        signed_up = Customer.objects.values('signup_time').all()
        signed_up = signed_up.filter(engeneer_id=engeneer_id)
        signed_up = signed_up.filter(signup_date=signup_date)

        #Not occupied send to form
        queryset = SignUpRange.objects.exclude(signup_time__in=signed_up).all()
        context['form'].fields['ranges'].queryset = queryset
        return context

    def form_valid(self, form):
        #Save the new customer object
        engeneer = Engeneer.objects.get(id=self.kwargs['eng_id'])
        customer = Customer(
            name=form.cleaned_data.get('name'),
            car=form.cleaned_data.get('car'),
            engeneer=engeneer,
            signup_date=self.kwargs['signup_date'],
            signup_time=form.cleaned_data.get('ranges'),
        )
        customer.save()
        return super().form_valid(form)
