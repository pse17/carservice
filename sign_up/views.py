from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from sign_up.forms import CustomerForm, EngeneerForm
from sign_up.models import Customer, SignUpRange, Engeneer

class EngeneerFormView(FormView):
    template_name = 'engeneer.html'
    form_class = EngeneerForm

    def form_valid(self, form):
        engeneer_id = form.data['engeneer']
        signup_date = form.data['signup_date']
        self.success_url = '/signup/%s/%s' % (engeneer_id, signup_date)
        return super().form_valid(form)

class CustomerFormView(FormView):
    template_name = 'customer.html'
    form_class = CustomerForm
    success_url = reverse_lazy('engeneer')

    def get_context_data(self, **kwargs):
        signup_date = self.kwargs['signup_date']
        engeneer_id = self.kwargs['eng_id']

        context = super(CustomerFormView, self).get_context_data(**kwargs)
        context['signup_date'] = signup_date

        signed_up = Customer.objects.filter(engeneer_id=engeneer_id).filter(signup_date=signup_date).values('signup_time').all()
        queryset = SignUpRange.objects.values('signup_time').difference(signed_up).all()

        #queryset = SignUpRange.objects.filter(signup_time='12:00').all()
        #queryset = SignUpRange.objects.all()
        context['form'].fields['ranges'].queryset = queryset
        return context

    def get_initial(self):
        intial = super(CustomerFormView, self).get_initial()
        #intial['ranges'] = SignUpRange.objects.get(id=2)
        return intial
    
    def form_valid(self, form):
        engeneer = Engeneer.objects.get(id=self.kwargs['eng_id'])
        customer = Customer(
            name = form.cleaned_data.get('name'),
            car = form.cleaned_data.get('car'),
            engeneer = engeneer,
            signup_date = self.kwargs['signup_date'],
            signup_time = form.cleaned_data.get('ranges'),
        )
        customer.save()
        return super().form_valid(form)
