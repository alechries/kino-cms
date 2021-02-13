from django.forms import Form, ModelForm, TextInput, CharField
from django.contrib.auth import get_user_model
from . import models


class LoginForm(Form):
    class Meta:
        model = models.User

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


class RegisterForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'retype_password']

    first_name = CharField(widget=TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Имя',
    }))
    last_name = CharField(widget=TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Фамилия',
    }))
    username = CharField(widget=TextInput(attrs={
        'class': "form-control",
        'type': "text",
        'placeholder': 'Никнейм для авторизации',
    }))
    email = CharField(widget=TextInput(attrs={
        'class': "form-control",
        'id': "InputEmail",
        'type': "email",
        'placeholder': 'Электронная почта',
    }))
    password = CharField(widget=TextInput(attrs={
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Пароль',
    }))
    retype_password = CharField(widget=TextInput(attrs={
        'type': 'password',
        'class': 'form-control',
        'placeholder': 'Повторите пароль',
    }))