from django.urls import path
from sign_up.views import CustomerFormView

urlpatterns = [
    path('signup', CustomerFormView.as_view(), name='signup')
]