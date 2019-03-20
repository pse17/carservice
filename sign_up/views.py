from django.shortcuts import render
from django.views.generic import FormView
from sign_up.forms import CustomerForm

class CustomerFormView(FormView):
    template_name = 'customer.html'
    form_class = CustomerForm
    success_url = '/'

    def form_valid(self, form):
        pass
        return super().form_valid(form)
