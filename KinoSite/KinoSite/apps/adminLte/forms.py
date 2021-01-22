from .models import Film
from django.forms import Form, ModelForm, TextInput, DateInput, FileInput, URLInput, CheckboxInput, Textarea, \
    EmailField, CharField, PasswordInput
from django.contrib.auth.forms import UserCreationForm
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


class RegisterForm(UserCreationForm):
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'main_image', 'image1', 'image2', 'image3', 'image4', 'image5', 'trailer_link',
                  'two_d', 'three_d', 'i_max', 'duration', 'first_night']


        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название фильма',
                'id': 'FilmNameInput',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'id': 'FilmTextInput',
                'rows': '5',
                'placeholder': 'Введите описание фильма',
            }),
            'main_image': FileInput(attrs={
                'class': 'form-control-file',
                'id': 'FilmPoster',
            }),
            'image1': FileInput(attrs={
                'class': 'form-control-file col-md-3 pl-0'
            }),
            'image2': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'image3': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'image4': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'image5': FileInput(attrs={
                'class': 'form-control-file col-md-3'
            }),
            'two_d': CheckboxInput(attrs={
                'name': 'two_d',
                'class': 'form-check-input',
                'type': 'checkbox',
                'id': 'inlineCheckbox1',
                'value': 'True',
            }),
            'three_d': CheckboxInput(attrs={
                'name': 'three_d',
                'class': 'form-check-input',
                'type': 'checkbox',
                'id': 'inlineCheckbox2',
                'value': 'True',
            }),
            'i_max': CheckboxInput(attrs={
                'name': 'i_max',
                'class': 'form-check-input',
                'type': 'checkbox',
                'id': 'inlineCheckbox3',
                'value': 'True',
            }),
            'duration': TextInput(attrs={
                'placeholder': 'Пример: 1 час 53 минуты',
                'class': 'form-control',
                'id': 'FilmDuration',
            }),
            'trailer_link': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку. Пример: https://www.youtube.com/watch...',
                'id': 'TrailerName',
            }),
            'first_night': DateInput(attrs={
                'type': "date",
                'placeholder': "Введите дату премьеры",
                'class': "form-control",
                'id': "FilmFirstNightDate",
        }),

        }