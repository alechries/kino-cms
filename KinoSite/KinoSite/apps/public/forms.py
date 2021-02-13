from django.forms import Form, TextInput, CharField
from django.contrib.auth.models import User


class LoginForm(Form):
    class Meta:
        model = User

    username = CharField(widget=TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Username',
            }))
    password = CharField(widget=TextInput(attrs={
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Password',
            }))