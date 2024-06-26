from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CriarUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    matricula = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "matricula"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
