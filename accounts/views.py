
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

# This makes the assumption that you have a urlpattern with
# the name 'login'.

class SignUpView(CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'
