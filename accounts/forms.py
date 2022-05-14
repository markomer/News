from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class UserCreationForm(UserCreationForm):
  class Meta(UserCreationForm):
    model = CustomUser
    fields = (
      UserCreationForm.Meta.fields + ('preferred_language', ))


class UserChangeForm(UserChangeForm):
  class Meta(UserChangeForm):
    model = CustomUser
    fields = UserChangeForm.Meta.fields    