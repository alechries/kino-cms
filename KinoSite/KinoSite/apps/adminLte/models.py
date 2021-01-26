from django.db import models
import os
from solo.models import SingletonModel


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


class BannerImage(models.Model):
    banner_image = models.ImageField('Изображение баннера')
    banner_url = models.URLField('Ссылка под изображением')
    banner_text = models.CharField('Описание изображения', null=True, max_length=255)


class UpperBanner(models.Model):
    upper_banner_image = models.ImageField('Верхний баннер', upload_to='images/upper_banner')


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


class CinemaHall(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    hall_name = models.CharField(max_length=255, verbose_name='Название зала')
    hall_description = models.TextField(verbose_name='Описание зала')
    cinema_scheme = models.ImageField(verbose_name='Схема зала', upload_to='images/hall/logo/')
    hall_upper_banner = models.ImageField('Верхний баннер кинотеатра', upload_to='images/hall/upper_banner/')
    hall_image1 = models.ImageField('Первое изображение', upload_to='images/hall/')
    hall_image2 = models.ImageField('Второе изображение', upload_to='images/hall/')
    hall_image3 = models.ImageField('Третее изображение', upload_to='images/hall/')
    hall_image4 = models.ImageField('Четвёртое изображение', upload_to='images/hall/')
    hall_image5 = models.ImageField('Пятое изображение', upload_to='images/hall/')
    hall_scheme = models.ImageField(verbose_name='Схема зала', upload_to='images/hall/logo/')

    def __str__(self):
        return self.hall_name


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
    news_status = models.CharField(verbose_name='Выбор статуса', max_length=3, choices=STATUS)

    def __str__(self):
        return self.news_name

    def get_absolute_image(self):
        return os.path.join('/media', self.news_main_image.name)

    def get_absolute_url(self):
        return f'news/list'


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
    promo_status = models.CharField(verbose_name='Выбор статуса',  max_length=3, choices=STATUS)

    def __str__(self):
        return self.promo_name


class Page(models.Model):
    class Meta:
        abstract = True

    page_name = models.CharField(max_length=255, verbose_name='Название страницы')
    page_description = models.TextField(verbose_name='Описание страницы')
    page_main_image = models.ImageField(verbose_name='Логотип страницы', upload_to='images/pages/logo')
    page_image1 = models.ImageField(verbose_name='Первое изображение', upload_to='images/pages/')
    page_image2 = models.ImageField(verbose_name='Второе изображение', upload_to='images/pages/')
    page_image3 = models.ImageField(verbose_name='Третее изображение', upload_to='images/pages/')
    page_image4 = models.ImageField(verbose_name='Четвёртое изображение', upload_to='images/pages/')
    page_image5 = models.ImageField(verbose_name='Пятое изображение', upload_to='images/pages/')
    page_status = models.BooleanField(verbose_name='Статус страницы', default=False)


class MainPage(SingletonModel):
    tel_number1 = models.IntegerField(verbose_name='Номер телефона')
    tel_number2 = models.IntegerField(verbose_name='Номер телефона')


class AboutCinema(SingletonModel):
    cinema_name = models.CharField(max_length=255, verbose_name='Название сети кинотеатров')
    cinema_description = models.TextField(verbose_name='Описание сети кинотеатров')
    cinema_main_image = models.ImageField(verbose_name='Логотип сети кинотеатров', upload_to='images/about/logo/')
    cinema_image1 = models.ImageField(verbose_name='Первое изображение', upload_to='images/about/')
    cinema_image2 = models.ImageField(verbose_name='Второе изображение', upload_to='images/about/')
    cinema_image3 = models.ImageField(verbose_name='Третее изображение', upload_to='images/about/')
    cinema_image4 = models.ImageField(verbose_name='Четвёртое изображение', upload_to='images/about/')
    cinema_image5 = models.ImageField(verbose_name='Пятое изображение', upload_to='images/about/')


class CafeBar(SingletonModel):
    cafebar_name = models.CharField(max_length=255, verbose_name='Название кафе-бара')
    cafebar_description = models.TextField(verbose_name='Описание кафе-бара')
    cafebar_main_image = models.ImageField(verbose_name='Логотип кафе-бара', upload_to='images/cafe_bar/logo/')
    cafebar_image1 = models.ImageField(verbose_name='Первое изображение', upload_to='images/cafe_bar/')
    cafebar_image2 = models.ImageField(verbose_name='Второе изображение', upload_to='images/cafe_bar/')
    cafebar_image3 = models.ImageField(verbose_name='Третее изображение', upload_to='images/cafe_bar/')
    cafebar_image4 = models.ImageField(verbose_name='Четвёртое изображение', upload_to='images/cafe_bar/')
    cafebar_image5 = models.ImageField(verbose_name='Пятое изображение', upload_to='images/cafe_bar/')


class VipHall(SingletonModel):
    hall_name = models.CharField(max_length=255, verbose_name='Название VIP-зала')
    hall_description = models.TextField(verbose_name='Описание VIP-зала')
    hall_main_image = models.ImageField(verbose_name='Логотип VIP-зала', upload_to='images/vip_hall/logo/')
    hall_image1 = models.ImageField(verbose_name='Первое изображение', upload_to='images/vip_hall/')
    hall_image2 = models.ImageField(verbose_name='Второе изображение', upload_to='images/vip_hall/')
    hall_image3 = models.ImageField(verbose_name='Третее изображение', upload_to='images/vip_hall/')
    hall_image4 = models.ImageField(verbose_name='Четвёртое изображение', upload_to='images/vip_hall/')
    hall_image5 = models.ImageField(verbose_name='Пятое изображение', upload_to='images/vip_hall/')


class Advertising(SingletonModel):
    adv_name = models.CharField(max_length=255, verbose_name='Название рекламы')
    adv_description = models.TextField(verbose_name='Описание рекламы')
    adv_main_image = models.ImageField(verbose_name='Логотип рекламы', upload_to='images/adv/logo/')
    adv_image1 = models.ImageField(verbose_name='Первое изображение', upload_to='images/adv/')
    adv_image2 = models.ImageField(verbose_name='Второе изображение', upload_to='images/adv/')
    adv_image3 = models.ImageField(verbose_name='Третее изображение', upload_to='images/adv/')
    adv_image4 = models.ImageField(verbose_name='Четвёртое изображение', upload_to='images/adv/')
    adv_image5 = models.ImageField(verbose_name='Пятое изображение', upload_to='images/adv/')


class ChildRoom(SingletonModel):
    room_name = models.CharField(max_length=255, verbose_name='Название детской комнаты')
    room_description = models.TextField(verbose_name='Описание детской комнаты')
    room_main_image = models.ImageField(verbose_name='Логотип детской комнаты', upload_to='images/child_room/logo/')
    room_image1 = models.ImageField(verbose_name='Первое изображение', upload_to='images/child_room/')
    room_image2 = models.ImageField(verbose_name='Второе изображение', upload_to='images/child_room/')
    room_image3 = models.ImageField(verbose_name='Третее изображение', upload_to='images/child_room/')
    room_image4 = models.ImageField(verbose_name='Четвёртое изображение', upload_to='images/child_room/')
    room_image5 = models.ImageField(verbose_name='Пятое изображение', upload_to='images/child_room/')


class Contact(models.Model):
    contact_name = models.CharField(verbose_name='Название кинотеатра', max_length=255)
    contact_address = models.TextField(verbose_name='Адрес кинотеатра')
    contact_location = models.CharField(verbose_name='Координаты для карты', max_length=255)
    contact_logo = models.ImageField(verbose_name='Лого', upload_to='images/contact/logo/')


class User(models.Model):
    LANGUAGE = (
        ('R', 'Rus'),
        ('U', 'Ukr'),
    )
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    CITY = (
        ('OD', 'Odessa'),
        ('KY', 'Kyiv'),
        ('KHAR', 'Kharkiv'),
    )

    name = models.CharField(verbose_name='Имя', max_length=255)
    surname = models.CharField(verbose_name='Фамиоия', max_length=255)
    username = models.CharField(verbose_name='Юзернейм', max_length=255)
    email = models.EmailField(verbose_name='Емаил')
    address = models.TextField(verbose_name='Адрес', max_length=255)
    password = models.CharField(verbose_name='Пароль', max_length=255)
    password2 = models.CharField(verbose_name='Пароль 2', max_length=255)
    card_number = models.CharField(verbose_name='Номер карты', max_length=255)
    language = models.CharField(verbose_name='Язык', max_length=1, choices=LANGUAGE)
    gender = models.CharField(verbose_name='Пол', max_length=1, choices=GENDER)
    city = models.CharField(verbose_name='Город', choices=CITY, max_length=4)