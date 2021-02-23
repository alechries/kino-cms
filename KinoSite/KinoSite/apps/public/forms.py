from . import models
from django.forms import Form, ModelForm, TextInput, DateInput, CharField, RadioSelect, PasswordInput
from django import forms
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import forms as django_forms


class LoginForm(Form):
    class Meta:
        model = models.User

    email = CharField(widget=TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'placeholder': 'Email',
    }))
    password = CharField(widget=TextInput(attrs={
        'type': 'password',
        'class': 'form-control',
        'placeholder': 'Password',
    }))


class RegisterForm(ModelForm):
    """
      A form that creates a user, with no privileges, from the given username and
      password.
      """
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Пароль'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Повтор пароля'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = models.User
        fields = ("email", "first_name", "last_name")
        field_classes = {
            'email': django_forms.UsernameField
        }
        widgets = {
            'email': TextInput(attrs={
                'type': "email",
                'placeholder': "Почта",
            }),
            'first_name': TextInput(attrs={
                'placeholder': "Имя",
            }),
            'last_name': TextInput(attrs={
                'placeholder': "Фамилия",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserForm(ModelForm):
    class Meta:
        model = models.User
        password2 = TextInput(attrs={
            'class': "form-control",
            'id': "InputPassword2",
            'placeholder': "Введите пароль",
        })
        fields = ['first_name', 'last_name', 'phone', 'email', 'address', 'password', 'card_number',
                  'language', 'gender', 'city', 'date_of_birth', 'gender']

        widgets = {
            'email': TextInput(attrs={
                'class': "form-control",
                'id': "InputEmail",
                'type': "email",
            }),
            'first_name': TextInput(attrs={
                'class': "form-control",
                'id': "InputFirstName",
            }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'id': "InputLastName",
            }),
            'phone': TextInput(attrs={
                'class': "form-control",
                'id': "InputPhone",
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
