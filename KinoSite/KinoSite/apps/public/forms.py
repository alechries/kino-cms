from django.forms import Form, ModelForm, TextInput, CharField
from django.contrib.auth import get_user_model
from . import models
from django.forms import Form, ModelForm, TextInput, DateInput, FileInput, URLInput, CheckboxInput, Textarea, \
    EmailField, CharField, RadioSelect, \
    TimeInput


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


class UserForm(ModelForm):
    class Meta:
        model = models.User
        password2 = TextInput(attrs={
            'class': "form-control",
            'id': "InputPassword2",
            'placeholder': "Введите пароль",
        })
        fields = ['first_name', 'last_name', 'phone', 'username', 'email', 'address', 'password', 'card_number',
                  'language', 'gender', 'city', 'date_of_birth', 'gender']

        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'id': "InputFirstName",
            }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'id': "InputLastName",
            }),
            'username': TextInput(attrs={
                'class': "form-control",
                'id': "InputUsername",
            }),
            'phone': TextInput(attrs={
                'class': "form-control",
                'id': "InputPhone",
            }),
            'email': TextInput(attrs={
                'class': "form-control",
                'id': "InputEmail",
                'type': "email",
            }),
            'date_of_birth': DateInput(format=('%Y-%m-%d'), attrs={
                'type': "date",
                'placeholder': "Введите дату рождения",
                'class': "form-control",
                'id': "InputDate",
            }),
            'address': TextInput(attrs={
                'class': "form-control",
                'id': "InputAddress",
            }),
            'password': TextInput(attrs={
                'class': "form-control",
                'id': "InputPassword",
                'type': "Password",
            }),
            'card_number': TextInput(attrs={
                'class': "form-control",
                'id': "InputCardNumber",
                'placeholder': "Пример: 1234 5678 9012 3456"
            }),
            'gender': RadioSelect(attrs={
                'class': 'custom-control-input  custom-control-label',
            }),
            'language': RadioSelect(attrs={
                'class': 'custom-control-input  custom-control-label',
            })
        }


class UserPasswordForm(Form):
    password = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Новый пароль',
        'id': 'PasswordInput',
        'type': 'Password'
    }))
