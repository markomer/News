from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm):
    model = CustomUser
    fields = (
      UserCreationForm.Meta.fields + ('preferred_language', ) + ('email', ))


class CustomUserChangeForm(UserChangeForm):
  class Meta(UserChangeForm):
    model = CustomUser
    fields = UserChangeForm.Meta.fields    