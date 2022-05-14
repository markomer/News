
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy


# This makes the assumption that you have a urlpattern with
# the name 'login'.

class SignUpView(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'
