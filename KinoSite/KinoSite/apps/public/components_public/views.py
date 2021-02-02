from django.shortcuts import render
from .. import models


def index(request):
    background_banner = models.BackgroundBanner.get_solo()
    return render(request, 'public/index.html', {'background_banner': background_banner})


def account_cabinet(request):
    return render(request, 'public/account/cabinet.html')


def account_login(request):
    return render(request, 'public/account/login.html')


def account_logout(request):
    # сделать редирект на главную страницу
    return render(request, 'public/base.html')


def account_registration(request):
    return render(request, 'public/account/registration.html')


def posters_films_list(request):
    return render(request, 'public/posters/films_list.html')


def posters_films_details(request):
    return render(request, 'public/posters/films_details.html')


def soon_list(request):
    return render(request, 'public/soon/list.html')


def timetable_films_sessions_list(request):
    return render(request, 'public/timetable/films-sessions-list.html')


def timetable_reservation(request, pk):
    return render(request, 'public/timetable/reservation.html')


def cinema_list(request):
    return render(request, 'public/cinema/list.html')


def cinema_details(request, pk):
    return render(request, 'public/cinema/details.html')


def cinema_hall_details(request, pk):
    return render(request, 'public/cinema/hall_details.html')


def promotion_list(request):
    return render(request, 'public/promotion/list.html')


def promotion_details(request, pk):
    return render(request, 'public/promotion/details.html')


def about_cinema(request):
    return render(request, 'public/about/cinema.html')


def about_news(request):
    return render(request, 'public/about/news.html')


def about_cafe_bar(request):
    return render(request, 'public/about/cafe-bar.html')


def about_vip_hall(request):
    return render(request, 'public/about/vip-hall.html')


def about_advertising(request):
    return render(request, 'public/about/advertising.html')


def about_mobile_app(request):
    return render(request, 'public/about/mobile-app.html')


def about_contacts(request):
    return render(request, 'public/about/contacts.html')