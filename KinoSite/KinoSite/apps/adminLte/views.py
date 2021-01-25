from .models import Film
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FilmForm, LoginForm
from . import models, forms

ADMIN_LOGIN_REDIRECT_URL = '/adminLte/account/login'


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def admin_index(request):
    return render(request, 'adminLte/index.html')


def account_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('admin_index')
                else:
                    _message = 'User is not active'
            else:
                _message = 'User does not exist'
        else:
            _message = 'Data is incorrect'
    else:
        _message = 'Please, Sign in'
    return render(request, 'adminLte/account/login.html', {'form': LoginForm(), 'message': _message})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def account_logout(request):
    logout(request)
    return redirect('admin_index')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def banner(request):
    return render(request, 'adminLte/banner.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def film_edit_form(request, pk=None):
    film = get_object_or_404(models.Film, pk=pk) if pk else None
    form = FilmForm(request.POST or None, request.FILES or None, instance=film or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin_film_list')
    return render(request, 'adminLte/film/film_form.html', {'form': form})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def film_list(request):
    films = models.Film.objects.all()

    return render(request, 'adminLte/film/film_list.html', {'film': films})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def film_delete(request, pk):
    films = models.Film.objects.filter(id=pk)
    films.delete()
    return redirect('admin_film_list')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def cinema_list(request):
    cinemas = models.Cinema.objects.all()
    return render(request, 'adminLte/cinema/cinema_list.html', {'cinemas': cinemas})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def cinema_form(request, pk=None):
    film = get_object_or_404(models.Cinema, pk=pk) if pk else None
    form = FilmForm(request.POST or None, request.FILES or None, instance=film or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin_film_list')
    return render(request, 'adminLte/film/film_form.html', {'form': form})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def cinema_delete(request, pk):
    cinema = models.Cinema.objects.filter(id=pk)
    cinema.delete()
    return redirect('admin_cinema_list')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def hall_form(request, pk=None):
    film = get_object_or_404(models.CinemaHall, pk=pk) if pk else None
    form = FilmForm(request.POST or None, request.FILES or None, instance=film or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin_film_list')
    return render(request, 'adminLte/film/film_form.html', {'form': form})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def hall_delete(request, pk):
    hall = models.CinemaHall.objects.filter(id=pk)
    hall.delete()
    return redirect('admin_cinema_list')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def news_list(request):
    return render(request, 'adminLte/news/news_list.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def news_page(request):
    return render(request, 'adminLte/news/news_page.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def promotion_list(request):
    return render(request, 'adminLte/promotion/promotion_list.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def promotion_page(request):
    return render(request, 'adminLte/promotion/promotion_page.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def pages_list(request):
    return render(request, 'adminLte/pages/pages_list.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def main_pages(request):
    return render(request, 'adminLte/pages/main_page.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def about_cinema(request):
    return render(request, 'adminLte/pages/about_cinema.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def cafe_bar(request):
    return render(request, 'adminLte/pages/cafe_bar.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def vip_room(request):
    return render(request, 'adminLte/pages/vip_room.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def ads(request):
    return render(request, 'adminLte/pages/ads.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def child_room(request):
    return render(request, 'adminLte/pages/child_room.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def contact(request):
    return render(request, 'adminLte/pages/contact.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def users_list(request):
    return render(request, 'adminLte/users/users_list.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def redact(request):
    return render(request, 'adminLte/users/users_edit.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def user_choose(request):
    return render(request, 'adminLte/mailing/user_choose.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def mailing(request):
    return render(request, 'adminLte/mailing/mailing.html')
