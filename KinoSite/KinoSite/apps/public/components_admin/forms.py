from .. import models
from django.forms import Form, ModelForm, TextInput, DateInput, FileInput, URLInput, CheckboxInput, Textarea, \
    EmailField, CharField, PasswordInput, ImageField, ModelChoiceField, URLField, ChoiceField, TimeField, BooleanField, RadioSelect, NumberInput, \
    TimeInput


from easy_maps.widgets import AddressWithMapWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper


class SEOForm(ModelForm):
    class Meta:
        model = models.SEO
        fields = ['seo_title', 'seo_keywords', 'seo_description']
        widgets = {
            'seo_title': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок',
                'rows': '5',
                'id': 'TitleInput',
            }),
            'seo_keywords': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ключевые слова',
                'rows': '5',
                'id': 'KeywordsInput',
            }),
            'seo_description': Textarea(attrs={
                'class': 'form-control',
                'id': 'DescriptionInput',
                'rows': '5',
                'placeholder': 'Введите описание',
            }),
        }


class FilmForm(ModelForm):
    class Meta:
        model = models.Film
        fields = ['title', 'description', 'main_image', 'image1',
                  'image2', 'image3', 'image4', 'image5', 'trailer_link',
                  'two_d', 'three_d', 'i_max', 'duration', 'first_night',
                  'original_title', 'country', 'director', 'language', 'type']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название фильма',
                'id': 'FilmNameInput',
            }),
            'original_title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите оригинальное название фильма',
                'id': 'FilmOriginalNameInput',
            }),
            'country': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите страну создания',
                'id': 'FilmCountryInput',
            }),
            'director': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите режиссера',
                'id': 'FilmDirectorInput',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'id': 'FilmTextInput',
                'rows': '5',
                'placeholder': 'Введите описание фильма',
            }),
            'main_image': FileInput(attrs={
                'class': 'upload',
                'id': 'FilmPoster',
            }),
            'image1': FileInput(attrs={
                'class': 'upload',
            }),
            'image2': FileInput(attrs={
                'class': 'upload',
            }),
            'image3': FileInput(attrs={
                'class': 'upload',
            }),
            'image4': FileInput(attrs={
                'class': 'upload',
            }),
            'image5': FileInput(attrs={
                'class': 'upload',
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
                'class': 'form-control col-md-7',
                'placeholder': 'Пример: 1.53',
                'type': "number",
                'step': "0.01",
                'id': 'FilmDuration',
            }),

            'first_night': DateInput(format=('%Y-%m-%d'), attrs={
                'type': "date",
                'placeholder': "Введите дату премьеры",
                'class': "form-control col-md-5",
                'id': "FilmFirstNightDate",
        }),

        }


class SessionForm(ModelForm):
    class Meta:
        model = models.FilmSession
        hall = ModelChoiceField(queryset=models.CinemaHall.objects.all(),  empty_label=None, to_field_name="hall")
        film = ModelChoiceField(queryset=models.Film.objects.all(),  empty_label=None, to_field_name="film")
        fields = ['hall', 'date', 'time', 'film', 'price', 'vip_price']
        widgets= {
            'date': DateInput(format=('%Y-%m-%d'), attrs={
                'type': "date",
                'placeholder': "Введите дату показа",
                'class': "form-control",
                'id': "FilmSessionDate",
            }),
            'time': TimeInput(format=('%H:%M'), attrs={
                'type': "time",
                'placeholder': "Введите время показа",
                'class': "form-control",
                'id': "FilmSessionTime",
            }),
            'price': NumberInput(attrs={
                'placeholder': "Введите стоимость показа",
                'class': "form-control",
                'id': "FilmSessionPrice",
            }),
            'vip_price': NumberInput(attrs={
                'placeholder': "Введите стоимость показа в вип-зале",
                'class': "form-control",
            }),

        }


class CinemaForm(ModelForm):
    class Meta:
        model = models.Cinema
        fields = ['cinema_name', 'cinema_description', 'cinema_condition', 'cinema_logo', 'cinema_upper_banner',
                  'cinema_image1', 'cinema_image2', 'cinema_image3', 'cinema_image4', 'cinema_image5']

        widgets = {
            'cinema_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название кинотеатра',
                'id': 'CinemaNameInput',
            }),
            'cinema_description': Textarea(attrs={
                'class': 'form-control',
                'id': 'CinemaDescriptionInput',
                'rows': '5',
                'placeholder': 'Введите описание кинотеатра',
            }),
            'cinema_condition': Textarea(attrs={
                'class': 'form-control',
                'id': 'CinemaConditionInput',
                'rows': '5',
                'placeholder': 'Введите условия кинотеатра',
            }),
            'cinema_logo': FileInput(attrs={
                'class': 'upload',
                'id': 'CinemaLogoInput',
            }),
            'cinema_upper_banner': FileInput(attrs={
                'class': 'upload',
                'id': 'CinemaUpperBannerInput',
            }),
            'cinema_image1': FileInput(attrs={
                'class': 'upload',
            }),
            'cinema_image2': FileInput(attrs={
                'class': 'upload',
            }),
            'cinema_image3': FileInput(attrs={
                'class': 'upload',
            }),
            'cinema_image4': FileInput(attrs={
                'class': 'upload',
            }),
            'cinema_image5': FileInput(attrs={
                'class': 'upload',
            })}


class CinemaHallForm(ModelForm):
    class Meta:
        model = models.CinemaHall
        cinema = ModelChoiceField(queryset=models.Cinema.objects.all(), empty_label=None, to_field_name="cinema_name")
        fields = ['cinema', 'hall_name', 'hall_description', 'hall_scheme', 'hall_upper_banner',
                  'hall_image1', 'hall_image2', 'hall_image3', 'hall_image4', 'hall_image5']

        widgets = {
            'hall_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название кинотеатра',
                'id': 'HallNameInput',
            }),
            'hall_description': Textarea(attrs={
                'class': 'form-control',
                'id': 'HallDescriptionInput',
                'rows': '5',
                'placeholder': 'Введите описание кинотеатра',
            }),
            'hall_scheme': FileInput(attrs={
                'class': 'upload',
                'id': 'HallSchemeInput',
            }),
            'hall_upper_banner': FileInput(attrs={
                'class': 'upload',
                'id': 'HallUpperBannerInput',
            }),
            'hall_image1': FileInput(attrs={
                'class': 'upload',
            }),
            'hall_image2': FileInput(attrs={
                'class': 'upload',
            }),
            'hall_image3': FileInput(attrs={
                'class': 'upload',
            }),
            'hall_image4': FileInput(attrs={
                'class': 'upload',
            }),
            'hall_image5': FileInput(attrs={
                'class': 'upload',
            })}


class NewsForm(ModelForm):
    class Meta:
        model = models.News

        fields = ['news_name', 'news_description', 'news_main_image', 'news_image1', 'news_image2', 'news_image3',
                  'news_image4', 'news_image5', 'news_url', 'news_published_date', 'news_status']

        widgets = {
            'news_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название новости',
                'id': 'NewsNameInput',
            }),
            'news_description': Textarea(attrs={
                'class': 'form-control',
                'id': 'NewsTextInput',
                'rows': '5',
                'placeholder': 'Введите описание новости',
            }),
            'news_main_image': FileInput(attrs={
                'class': 'upload',
                'id': 'NewsMainImage',
            }),
            'news_image1': FileInput(attrs={
                'class': 'upload',
            }),
            'news_image2': FileInput(attrs={
                'class': 'upload',
            }),
            'news_image3': FileInput(attrs={
                'class': 'upload',
            }),
            'news_image4': FileInput(attrs={
                'class': 'upload',
            }),
            'news_image5': FileInput(attrs={
                'class': 'upload',
            }),
            'news_url': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на новость',
                'id': 'NewsUrl',
            }),
            'news_published_date': DateInput(format=('%Y-%m-%d'), attrs={
                'type': "date",
                'placeholder': "Введите дату публикации",
                'class': "form-control",
                'id': "NewsPublishedDate",
            }),
        }


class PromotionForm(ModelForm):
    class Meta:
        model = models.Promotion

        fields = ['promo_name', 'promo_description', 'promo_main_image', 'promo_image1', 'promo_image2', 'promo_image3',
                  'promo_image4', 'promo_image5', 'promo_url', 'promo_published_date', 'promo_status']

        widgets = {
            'promo_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название акции',
                'id': 'PromotionNameInput',
            }),
            'promo_description': Textarea(attrs={
                'class': 'form-control',
                'id': 'PromotionTextInput',
                'rows': '5',
                'placeholder': 'Введите описание акции',
            }),
            'promo_main_image': FileInput(attrs={
                'class': 'upload',
                'id': 'PromotionMainImage',
            }),
            'promo_image1': FileInput(attrs={
                'class': 'upload',
            }),
            'promo_image2': FileInput(attrs={
                'class': 'upload',
            }),
            'promo_image3': FileInput(attrs={
                'class': 'upload',
            }),
            'promo_image4': FileInput(attrs={
                'class': 'upload',
            }),
            'promo_image5': FileInput(attrs={
                'class': 'upload',
            }),
            'promo_url': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на акцию',
                'id': 'PromotionUrl',
            }),
            'promo_published_date': DateInput(format=('%Y-%m-%d'), attrs={
                'type': "date",
                'placeholder': "Введите дату публикации",
                'class': "form-control",
                'id': "PromotionPublishedDate",
            }),
        }


class MainPageForm(ModelForm):
    class Meta:
        model = models.MainPage
        fields = ['tel_number1', 'tel_number2', 'status']
        widgets = {
            'tel_number1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00000000',
                'id': 'TelNumber1Input',
            }),
            'tel_number2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00000000',
                'id': 'TelNumber2Input',
            }),
        }


class AboutCinemaForm(ModelForm):
    class Meta:
        model = models.AboutCinema

        fields = ['cinema_name', 'cinema_description', 'cinema_main_image', 'cinema_image1', 'cinema_image2',
                  'cinema_image3', 'cinema_image4', 'cinema_image5', 'status']

        widgets = {
            'cinema_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название сети кинотеатров',
                'id': 'AboutNameInput',
            }),
            'cinema_description': Textarea(attrs={
                'class': 'form-control',
                'id': 'AboutTextInput',
                'rows': '5',
                'placeholder': 'Введите описание сети кинотеатров',
            }),
            'cinema_main_image': FileInput(attrs={
                'class': 'upload',
                'id': 'AboutMainImage',
            }),
            'cinema_image1': FileInput(attrs={
                'class': 'upload',
            }),
            'cinema_image2': FileInput(attrs={
                'class': 'upload',
            }),
            'cinema_image3': FileInput(attrs={
                'class': 'upload',
            }),
            'cinema_image4': FileInput(attrs={
                'class': 'upload',
            }),
            'cinema_image5': FileInput(attrs={
                'class': 'upload',
            }),
        }


class CafeBarForm(ModelForm):
    class Meta:
        model = models.CafeBar

        fields = ['cafebar_name', 'cafebar_description', 'cafebar_main_image', 'cafebar_image1', 'cafebar_image2',
                  'cafebar_image3', 'cafebar_image4', 'cafebar_image5', 'status']

        widgets = {
            'cafebar_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название кафе-бара',
                'id': 'CafeBarNameInput',
            }),
            'cafebar_description': Textarea(attrs={
                'class': 'form-control',
                'id': 'CafeBarTextInput',
                'rows': '5',
                'placeholder': 'Введите описание кафе-бара',
            }),
            'cafebar_main_image': FileInput(attrs={
                'class': 'upload',
                'id': 'CafeBarMainImage',
            }),
            'cafebar_image1': FileInput(attrs={
                'class': 'upload',
            }),
            'cafebar_image2': FileInput(attrs={
                'class': 'upload',
            }),
            'cafebar_image3': FileInput(attrs={
                'class': 'upload',
            }),
            'cafebar_image4': FileInput(attrs={
                'class': 'upload',
            }),
            'cafebar_image5': FileInput(attrs={
                'class': 'upload',
            }),
        }


class VipHallForm(ModelForm):
    class Meta:
        model = models.VipHall

        fields = ['hall_name', 'hall_description', 'hall_main_image', 'hall_image1', 'hall_image2',
                  'hall_image3', 'hall_image4', 'hall_image5', 'status']

        widgets = {
            'hall_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название VIP-зала',
                'id': 'VipHallNameInput',
            }),
            'hall_description': Textarea(attrs={
                'class': 'form-control',
                'id': 'VipHallTextInput',
                'rows': '5',
                'placeholder': 'Введите описание VIP-зала',
            }),
            'hall_main_image': FileInput(attrs={
                'class': 'upload',
                'id': 'VipHallMainImage',
            }),
            'hall_image1': FileInput(attrs={
                'class': 'upload',
            }),
            'hall_image2': FileInput(attrs={
                'class': 'upload',
            }),
            'hall_image3': FileInput(attrs={
                'class': 'upload',
            }),
            'hall_image4': FileInput(attrs={
                'class': 'upload',
            }),
            'hall_image5': FileInput(attrs={
                'class': 'upload',
            }),
        }


class AdvertisingForm(ModelForm):
    class Meta:
        model = models.Advertising

        fields = ['adv_name', 'adv_description', 'adv_main_image', 'adv_image1', 'adv_image2',
                  'adv_image3', 'adv_image4', 'adv_image5', 'status']

        widgets = {
            'adv_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название рекламы',
                'id': 'AdvNameInput',
            }),
            'adv_description': Textarea(attrs={
                'class': 'form-control',
                'id': 'AdvTextInput',
                'rows': '5',
                'placeholder': 'Введите описание рекламы',
            }),
            'adv_main_image': FileInput(attrs={
                'class': 'upload',
                'id': 'AdvMainImage',
            }),
            'adv_image1': FileInput(attrs={
                'class': 'upload',
            }),
            'adv_image2': FileInput(attrs={
                'class': 'upload',
            }),
            'adv_image3': FileInput(attrs={
                'class': 'upload',
            }),
            'adv_image4': FileInput(attrs={
                'class': 'upload',
            }),
            'adv_image5': FileInput(attrs={
                'class': 'upload',
            }),
        }


class ChildRoomForm(ModelForm):
    class Meta:
        model = models.ChildRoom

        fields = ['room_name', 'room_description', 'room_main_image', 'room_image1', 'room_image2',
                  'room_image3', 'room_image4', 'room_image5', 'status']

        widgets = {
            'room_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название детской комнаты',
                'id': 'RoomNameInput',
            }),
            'room_description': Textarea(attrs={
                'class': 'form-control',
                'id': 'RoomTextInput',
                'rows': '5',
                'placeholder': 'Введите описание детской комнаты',
            }),
            'room_main_image': FileInput(attrs={
                'class': 'upload',
                'id': 'RoomMainImage',
            }),
            'room_image1': FileInput(attrs={
                'class': 'upload',
            }),
            'room_image2': FileInput(attrs={
                'class': 'upload',
            }),
            'room_image3': FileInput(attrs={
                'class': 'upload',
            }),
            'room_image4': FileInput(attrs={
                'class': 'upload',
            }),
            'room_image5': FileInput(attrs={
                'class': 'upload',
            }),
        }


class ContactForm(ModelForm):
    class Meta:
        model = models.Contact
        contact_cinema = ModelChoiceField(queryset=models.Cinema.objects.all(), empty_label=None, to_field_name="cinema_name")
        fields = ['contact_cinema', 'contact_address', 'contact_location', 'contact_logo', 'status']

        widgets = {
            'contact_address': Textarea(attrs={
                'class': 'form-control',
                'id': 'ContactAddressInput',
                'rows': '5',
                'placeholder': 'Введите адрес кинотеатра',
            }),
            'contact_location': AddressWithMapWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Введите координаты карты',
                'id': 'ContactCoordInput',
            }),
            'contact_logo': FileInput(attrs={
                'class': 'upload',
                'id': 'ContactMainImage',
            })
        }


class MainSlideForm(ModelForm):
    class Meta:
        model = models.MainSlide
        fields = ['slide_text', 'slide_image', 'slide_url', 'slide_timer']

        widgets = {
            'slide_image': FileInput(attrs={
                'class': 'upload',
                'id': 'MainSlideImage',
            }),
            'slide_text': Textarea(attrs={
                'class': "form-control",
                'rows': '5',
                'id': "MainSlideText",
            }),
            'slide_url': URLInput(attrs={
                'class': 'form-control',
                'id': 'MainSlideURL',
                'placeholder': 'Введите ссылку слайда',
            }),
            'slide_timer': TextInput(attrs={
                'class': 'form-control',
                'id': 'NewsPromoNumber',
                'placeholder': 'Введите cкорость',
            }),

        }


class NewsPromoSlideForm(ModelForm):
    class Meta:
        model = models.NewsPromoSlide
        fields = ['slide_text', 'slide_image', 'slide_url', 'slide_timer']

        widgets = {
            'slide_image': FileInput(attrs={
                'class': 'upload',
                'id': 'MainSlideImage',
            }),
            'slide_text': Textarea(attrs={
                'class': "form-control",
                'rows': '5',
                'id': "MainSlideText",
            }),
            'slide_url': URLInput(attrs={
                'class': 'form-control',
                'id': 'MainSlideURL',
                'placeholder': 'Введите ссылку слайда',
            }),
            'slide_timer': TextInput(attrs={
                'class': 'form-control',
                'id': 'NewsPromoNumber',
                'placeholder': 'Введите cкорость',
            }),

        }


class BackgroundBannerForm(ModelForm):
    class Meta:
        model = models.BackgroundBanner
        fields = ['banner_image',]

        widgets = {
            'banner_image': FileInput(attrs={
                'class': 'upload',
                'id': 'BannerImage',
            }),
        }


class MobileAppForm(ModelForm):
    class Meta:
        model = models.MobileApp
        fields = ['app_name', 'app_description', 'app_main_image', 'app_image1',
                  'app_image2', 'app_image3', 'app_image4', 'app_image5', 'app_apple', 'app_google', 'status']

        widgets = {
            'app_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название мобильного приложение',
                'id': 'NameInput',
            }),
            'app_description': Textarea(attrs={
                'class': 'form-control',
                'id': 'TextInput',
                'rows': '5',
                'placeholder': 'Введите описание мобильного приложение',
            }),
            'app_main_image': FileInput(attrs={
                'class': 'upload',
                'id': 'Poster',
            }),
            'app_image1': FileInput(attrs={
                'class': 'upload',
            }),
            'app_image2': FileInput(attrs={
                'class': 'upload',
            }),
            'app_image3': FileInput(attrs={
                'class': 'upload',
            }),
            'app_image4': FileInput(attrs={
                'class': 'upload',
            }),
            'app_image5': FileInput(attrs={
                'class': 'upload',
            }),
            'app_apple': URLInput(attrs={
                'class': 'form-control',
                'id': 'MainSlideURL',
                'placeholder': 'Введите ссылку на приложение из AppStore',
            }),
            'app_google': URLInput(attrs={
                'class': 'form-control',
                'id': 'MainSlideURL',
                'placeholder': 'Введите ссылку на приложение из PlayMarket',
            }),

        }


class ContextualAdvertisingForm(ModelForm):
    class Meta:
        model = models.ContextualAdvertising
        fields = ['link', 'horizontal_adv', 'vertical_adv']

        widgets = {
            'link': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку рекламы',
            }),
            'horizontal_adv': FileInput(attrs={
                'class': 'upload',
            }),
            'vertical_adv': FileInput(attrs={
                'class': 'upload',
            }),

        }