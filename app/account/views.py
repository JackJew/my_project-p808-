from account.models import Account
from django.urls import reverse_lazy
from django.views import generic
from .forms import  UserRegisterForm

class AccountRegistrationView(generic.CreateView):

    template_name = "account/register.html"
    form_class = UserRegisterForm
    model = Account
    success_url = reverse_lazy('index') # '/'
 
 
  