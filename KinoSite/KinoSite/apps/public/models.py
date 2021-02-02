
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User as DjangoUser, AbstractBaseUser, PermissionsMixin, AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from solo.models import SingletonModel
import os
from . import services
from .managers import CustomUserManager


############################################################
# EVENTS


@receiver(models.signals.post_delete)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    try:
        for file in instance.file_list():
            if file:
                services.delete_file_with_instance(file)
    except AttributeError:
        pass


@receiver(models.signals.pre_save)
def auto_delete_file_on_change(sender, instance, **kwargs):
    try:
        if not instance.pk:
            return False

        try:
            old_files = sender.objects.get(pk=instance.pk).file_list()
        except sender.DoesNotExist:
            return False

        new_files = instance.file_list()
        for index, new_file in enumerate(new_files):
            if not new_file == old_files[index]:
                services.delete_file_with_instance(old_files[index])
    except AttributeError:
        pass


############################################################
# MODELS


class User(AbstractUser):
    R = 1
    U = 2
    LANGUAGE = (
        ('R', 'Rus'),
        ('U', 'Ukr'),
    )
    M = 1
    F = 2
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    CITY = (
        ('OD', 'Одесса'),
        ('KY', 'Киев'),
        ('KHAR', 'Харьков'),
    )

    phone = models.CharField(verbose_name='Номер телефона', max_length=60)
    address = models.TextField(verbose_name='Адрес', max_length=255)
    card_number = models.CharField(verbose_name='Номер карты', max_length=255)
    language = models.CharField(verbose_name='Язык', max_length=1, choices=LANGUAGE, default=R)
    gender = models.CharField(verbose_name='Пол', max_length=1, choices=GENDER, default=M)
    city = models.CharField(verbose_name='', choices=CITY, max_length=4) #пустой вербоус нейм, конфликт с crispy forms
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True)

    def __str__(self):
        return self.username


class Film(models.Model):
    title = models.CharField('Название фильма', max_length=255)
    description = models.TextField('Описание фильма')
    main_image = models.ImageField(upload_to='images/film_poster')
    image1 = models.ImageField('Первое изображение', upload_to='images/film_images')
    image2 = models.ImageField('Второе изображение', upload_to='images/film_images/')
    image3 = models.ImageField('Третее изображение', upload_to='images/film_images/')
    image4 = models.ImageField('Четвёртое изображение', upload_to='images/film_images/')
    image5 = models.ImageField('Пятое изображение', upload_to='images/film_images/')
    trailer_link = models.URLField('Ссылка на трейлер')
    two_d = models.BooleanField('2Д', null=False)
    three_d = models.BooleanField('3Д', null=False)
    i_max = models.BooleanField('I_MAX', null=False)
    duration = models.CharField('Длительность фильма', max_length=55)
    first_night = models.DateField(verbose_name='Дата премьеры')

    def __str__(self):
        return self.title

    def get_absolute_image(self):
        return os.path.join('/media', self.main_image.name)

    def get_absolute_url(self):
        return f'film/list'

    def file_list(self):
        return [self.main_image, self.image1, self.image2, self.image3, self.image4, self.image5]


class Cinema(models.Model):
    cinema_name = models.CharField(max_length=255, verbose_name='Название кинотеатра')
    cinema_description = models.TextField(verbose_name='Описание конотеатра')
    cinema_condition = models.TextField(verbose_name='Условия кинотеатра')
    cinema_logo = models.ImageField(verbose_name='Логотип кинотеатра', upload_to='images/cinema/logo/')
    cinema_upper_banner = models.ImageField('Верхний баннер кинотеатра', upload_to='images/cinema/upper_banner/')
    cinema_image1 = models.ImageField('Первое изображение', upload_to='images/cinema/')
    cinema_image2 = models.ImageField('Второе изображение', upload_to='images/cinema/')
    cinema_image3 = models.ImageField('Третее изображение', upload_to='images/cinema/')
    cinema_image4 = models.ImageField('Четвёртое изображение', upload_to='images/cinema/')
    cinema_image5 = models.ImageField('Пятое изображение', upload_to='images/cinema/')

    def __str__(self):
        return self.cinema_name

    def file_list(self):
        return [self.cinema_logo, self.cinema_upper_banner, self.cinema_image1, self.cinema_image2, self.cinema_image3, self.cinema_image4, self.cinema_image5]


class CinemaHall(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name='') #пустой вербоус нейм, конфликт с crispy forms
    hall_name = models.CharField(max_length=255, verbose_name='Название зала')
    hall_description = models.TextField(verbose_name='Описание зала')
    cinema_scheme = models.ImageField(verbose_name='Схема кинотеатра', upload_to='images/hall/logo/')
    hall_upper_banner = models.ImageField('Верхний баннер кинотеатра', upload_to='images/hall/upper_banner/')
    hall_image1 = models.ImageField('Первое изображение', upload_to='images/hall/')
    hall_image2 = models.ImageField('Второе изображение', upload_to='images/hall/')
    hall_image3 = models.ImageField('Третее изображение', upload_to='images/hall/')
    hall_image4 = models.ImageField('Четвёртое изображение', upload_to='images/hall/')
    hall_image5 = models.ImageField('Пятое изображение', upload_to='images/hall/')
    hall_scheme = models.ImageField(verbose_name='Схема зала', upload_to='images/hall/logo/')

    def __str__(self):
        return self.hall_name

    def file_list(self):
        return [self.hall_upper_banner, self.hall_image1, self.hall_image2, self.hall_image3, self.hall_image4, self.hall_image5, self.hall_scheme]


class News(models.Model):
    STATUS = (
        ('ON', 'Active'),
        ('OFF', 'Inactive'),
    )

    news_name = models.CharField(max_length=255, verbose_name='Название новости')
    news_description = models.TextField(verbose_name='Описание новости')
    news_main_image = models.ImageField(verbose_name='Логотип новости', upload_to='images/news/logo/')
    news_image1 = models.ImageField(verbose_name='Первое изображение', upload_to='images/news/')
    news_image2 = models.ImageField(verbose_name='Второе изображение', upload_to='images/news/')
    news_image3 = models.ImageField(verbose_name='Третее изображение', upload_to='images/news/')
    news_image4 = models.ImageField(verbose_name='Четвёртое изображение', upload_to='images/news/')
    news_image5 = models.ImageField(verbose_name='Пятое изображение', upload_to='images/news/')
    news_url = models.URLField(verbose_name='Ссылка на видео', null=True)
    news_published_date = models.DateField(verbose_name='Дата публикации новости')
    news_status = models.CharField(verbose_name='', max_length=3, choices=STATUS) #пустой вербоус нейм, конфликт с crispy forms

    def __str__(self):
        return self.news_name

    def get_absolute_image(self):
        return os.path.join('/media', self.news_main_image.name)

    def get_absolute_url(self):
        return f'news/list'

    def file_list(self):
        return [self.news_main_image, self.news_image1, self.news_image2, self.news_image3, self.news_image4, self.news_image5]


class Promotion(models.Model):
    STATUS = (
        ('ON', 'Active'),
        ('OFF', 'Inactive'),
    )

    promo_name = models.CharField(max_length=255, verbose_name='Название акции')
    promo_description = models.TextField(verbose_name='Описание акции')
    promo_main_image = models.ImageField(verbose_name='Логотип акции', upload_to='images/promotion/logo/')
    promo_image1 = models.ImageField(verbose_name='Первое изображение', upload_to='images/promotion/')
    promo_image2 = models.ImageField(verbose_name='Второе изображение', upload_to='images/promotion/')
    promo_image3 = models.ImageField(verbose_name='Третее изображение', upload_to='images/promotion/')
    promo_image4 = models.ImageField(verbose_name='Четвёртое изображение', upload_to='images/promotion/')
    promo_image5 = models.ImageField(verbose_name='Пятое изображение', upload_to='images/promotion/')
    promo_url = models.URLField(verbose_name='Ссылка на акцию', null=True)
    promo_published_date = models.DateField(verbose_name='Дата публикации акции')
    promo_status = models.CharField(verbose_name='',  max_length=3, choices=STATUS) #пустой вербоус нейм, конфликт с crispy forms

    def __str__(self):
        return self.promo_name

    def file_list(self):
        return [self.promo_main_image, self.promo_image1, self.promo_image2, self.promo_image3, self.promo_image4, self.promo_image5]


class MainPage(SingletonModel):
    tel_number1 = models.IntegerField(verbose_name='Номер телефона', null=True)
    tel_number2 = models.IntegerField(verbose_name='Номер телефона', null=True)


class AboutCinema(SingletonModel):
    cinema_name = models.CharField(max_length=255, verbose_name='Название сети кинотеатров')
    cinema_description = models.TextField(verbose_name='Описание сети кинотеатров')
    cinema_main_image = models.ImageField(verbose_name='Логотип сети кинотеатров', upload_to='images/about/logo/')
    cinema_image1 = models.ImageField(verbose_name='Первое изображение', upload_to='images/about/')
    cinema_image2 = models.ImageField(verbose_name='Второе изображение', upload_to='images/about/')
    cinema_image3 = models.ImageField(verbose_name='Третее изображение', upload_to='images/about/')
    cinema_image4 = models.ImageField(verbose_name='Четвёртое изображение', upload_to='images/about/')
    cinema_image5 = models.ImageField(verbose_name='Пятое изображение', upload_to='images/about/')

    def file_list(self):
        return [self.cinema_main_image, self.cinema_image1, self.cinema_image2, self.cinema_image3, self.cinema_image4, self.cinema_image5]

    def __str__(self):
        return self.cinema_name


class CafeBar(SingletonModel):
    cafebar_name = models.CharField(max_length=255, verbose_name='Название кафе-бара')
    cafebar_description = models.TextField(verbose_name='Описание кафе-бара')
    cafebar_main_image = models.ImageField(verbose_name='Логотип кафе-бара', upload_to='images/cafe_bar/logo/')
    cafebar_image1 = models.ImageField(verbose_name='Первое изображение', upload_to='images/cafe_bar/')
    cafebar_image2 = models.ImageField(verbose_name='Второе изображение', upload_to='images/cafe_bar/')
    cafebar_image3 = models.ImageField(verbose_name='Третее изображение', upload_to='images/cafe_bar/')
    cafebar_image4 = models.ImageField(verbose_name='Четвёртое изображение', upload_to='images/cafe_bar/')
    cafebar_image5 = models.ImageField(verbose_name='Пятое изображение', upload_to='images/cafe_bar/')

    def file_list(self):
        return [self.cafebar_main_image, self.cafebar_image1, self.cafebar_image2, self.cafebar_image3, self.cafebar_image4, self.cafebar_image5]

    def __str__(self):
        return self.cafebar_name

class VipHall(SingletonModel):
    hall_name = models.CharField(max_length=255, verbose_name='Название VIP-зала')
    hall_description = models.TextField(verbose_name='Описание VIP-зала')
    hall_main_image = models.ImageField(verbose_name='Логотип VIP-зала', upload_to='images/vip_hall/logo/')
    hall_image1 = models.ImageField(verbose_name='Первое изображение', upload_to='images/vip_hall/')
    hall_image2 = models.ImageField(verbose_name='Второе изображение', upload_to='images/vip_hall/')
    hall_image3 = models.ImageField(verbose_name='Третее изображение', upload_to='images/vip_hall/')
    hall_image4 = models.ImageField(verbose_name='Четвёртое изображение', upload_to='images/vip_hall/')
    hall_image5 = models.ImageField(verbose_name='Пятое изображение', upload_to='images/vip_hall/')

    def file_list(self):
        return [self.hall_main_image, self.hall_image1, self.hall_image2, self.hall_image3, self.hall_image4, self.hall_image5]

    def __str__(self):
        return self.hall_name


class Advertising(SingletonModel):
    adv_name = models.CharField(max_length=255, verbose_name='Название рекламы')
    adv_description = models.TextField(verbose_name='Описание рекламы')
    adv_main_image = models.ImageField(verbose_name='Логотип рекламы', upload_to='images/adv/logo/')
    adv_image1 = models.ImageField(verbose_name='Первое изображение', upload_to='images/adv/')
    adv_image2 = models.ImageField(verbose_name='Второе изображение', upload_to='images/adv/')
    adv_image3 = models.ImageField(verbose_name='Третее изображение', upload_to='images/adv/')
    adv_image4 = models.ImageField(verbose_name='Четвёртое изображение', upload_to='images/adv/')
    adv_image5 = models.ImageField(verbose_name='Пятое изображение', upload_to='images/adv/')

    def file_list(self):
        return [self.adv_main_image, self.adv_image1, self.adv_image2, self.adv_image3, self.adv_image4, self.adv_image5]

    def __str__(self):
        return self.adv_name


class ChildRoom(SingletonModel):
    room_name = models.CharField(max_length=255, verbose_name='Название детской комнаты')
    room_description = models.TextField(verbose_name='Описание детской комнаты')
    room_main_image = models.ImageField(verbose_name='Логотип детской комнаты', upload_to='images/child_room/logo/')
    room_image1 = models.ImageField(verbose_name='Первое изображение', upload_to='images/child_room/')
    room_image2 = models.ImageField(verbose_name='Второе изображение', upload_to='images/child_room/')
    room_image3 = models.ImageField(verbose_name='Третее изображение', upload_to='images/child_room/')
    room_image4 = models.ImageField(verbose_name='Четвёртое изображение', upload_to='images/child_room/')
    room_image5 = models.ImageField(verbose_name='Пятое изображение', upload_to='images/child_room/')

    def file_list(self):
        return [self.room_main_image, self.room_image1, self.room_image1, self.room_image2, self.room_image3, self.room_image4, self.room_image5]

    def __str__(self):
        return self.room_name

class Contact(models.Model):
    contact_name = models.CharField(verbose_name='Название кинотеатра', max_length=255)
    contact_address = models.TextField(verbose_name='Адрес кинотеатра')
    contact_location = models.CharField(verbose_name='Координаты для карты', max_length=255)
    contact_logo = models.ImageField(verbose_name='Лого', upload_to='images/contact/logo/')

    def file_list(self):
        return [self.contact_logo, ]

    def __str__(self):
        return self.contact_name

class MainSlide(models.Model):
    slide_text = models.TextField(verbose_name='Текст слайда')
    slide_image = models.ImageField(verbose_name='Изображение слайда', upload_to='images/main_slide/')
    slide_url = models.URLField(verbose_name='Ссылка слайда')
    slide_timer = models.TextField(verbose_name='Скорость вращения')

    def get_absolute_image(self):
        return os.path.join('/media', self.slide_image.name)


    def file_list(self):
        return [self.slide_image, ]

    def __str__(self):
        return self.slide_url


class NewsPromoSlide(models.Model):
    slide_text = models.TextField(verbose_name='Текст слайда')
    slide_image = models.ImageField(verbose_name='Изображение слайда', upload_to='images/news_promo/')
    slide_url = models.URLField(verbose_name='Ссылка слайда')
    slide_timer = models.IntegerField(verbose_name='Скорость вращения')

    def file_list(self):
        return [self.slide_image, ]

    def __str__(self):
        return self.slide_url

    def get_absolute_image(self):
        return os.path.join('/media', self.slide_image.name)


class BackgroundBanner(SingletonModel):
    banner_image = models.ImageField(verbose_name='Изображение фона', upload_to='images/background/')

    def file_list(self):
        return [self.banner_image, ]

    def __str__(self):
        return self.banner_image

    def get_absolute_image(self):
        return os.path.join('/media/', self.banner_image.name)

