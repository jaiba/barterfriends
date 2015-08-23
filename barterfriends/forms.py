from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserRegister(UserCreationForm):
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = User
        fields = ('username', 'email',)
