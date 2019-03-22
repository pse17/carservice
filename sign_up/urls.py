from django.urls import path
from sign_up.views import EngeneerFormView, CustomerFormView

urlpatterns = [
    path('', EngeneerFormView.as_view(), name='engeneer'),
    path('signup/<int:eng_id>/<signup_date>', CustomerFormView.as_view(), name='customer')
]
