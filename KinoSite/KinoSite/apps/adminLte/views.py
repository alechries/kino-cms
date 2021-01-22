from .models import Film
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FilmForm, RegisterForm, LoginForm
from .models import Film


@login_required(login_url='/adminLte/account/login')
def index(request):
    return render(request, 'adminLte/index.html')


def account_login(request):
    if request.POST.get:
        form = LoginForm(request.POST)
        _message = 'Please sign in :)'
        if form.is_valid():
            cleaned_data: dict = form.cleaned_data
            if len(cleaned_data) > 0:
                username = cleaned_data['username']
                password = cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('admin_index')
                    else:
                        _message = 'Your account is not activated'
                else:
                    _message = 'Invalid login, please try again'
    else:
        form = LoginForm()
        _message = 'Please sign in'
    context = {'message': _message, 'form': form}
    return render(request, 'adminLte/account/login.html', context)


def account_register(request):
    form = RegisterForm()
    return render(request, 'adminLte/account/register.html', {'form': form})


@login_required(login_url='/adminLte/account/login')
def banner(request):
    return render(request, 'adminLte/banner.html')


@login_required(login_url='/adminLte/account/login')
def film_edit_form_post(request):
    form = FilmForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('film_list')


@login_required(login_url='/adminLte/account/login')
def film_edit_form_get(request, pk=None):
    if pk is not None:
        film = get_object_or_404(Film, pk=pk)
        form = FilmForm(instance=film)
    else:
        form = FilmForm()

    return render(request, 'adminLte/film/film_form.html', {'form': form})


@login_required(login_url='/adminLte/account/login')
def film_edit_form(request, pk=None):
    if request.method == 'POST':
        response = film_edit_form_post(request)
    elif request.method == 'GET':
        response = film_edit_form_get(request, pk)
    else:
        response = redirect('film_list')
    return response


@login_required(login_url='/adminLte/account/login')
def film_list(request):
    film = Film.objects.all()

    return render(request, 'adminLte/film/film_list.html', {'film': film})


@login_required(login_url='/adminLte/account/login')
def film_delete(request, pk):
    film = Film.objects.filter(id=pk)
    film.delete()
    return redirect('film_list')


@login_required(login_url='/adminLte/account/login')
def cinema_list(request):
    return render(request, 'adminLte/cinema/cinema_list.html')


@login_required(login_url='/adminLte/account/login')
def cinema_page(request):
    return redirect(request, 'adminLte/cinema/cinema_page.html')


@login_required(login_url='/adminLte/account/login')
def hall_page(request):
    return render(request, 'adminLte/cinema/hall_page.html')


@login_required(login_url='/adminLte/account/login')
def news_list(request):
    return render(request, 'adminLte/news/news_list.html')


@login_required(login_url='/adminLte/account/login')
def news_page(request):
    return render(request, 'adminLte/news/news_page.html')


@login_required(login_url='/adminLte/account/login')
def promotion_list(request):
    return render(request, 'adminLte/promotion/promotion_list.html')


@login_required(login_url='/adminLte/account/login')
def promotion_page(request):
    return render(request, 'adminLte/promotion/promotion_page.html')


@login_required(login_url='/adminLte/account/login')
def pages_list(request):
    return render(request, 'adminLte/pages/pages_list.html')


@login_required(login_url='/adminLte/account/login')
def main_pages(request):
    return render(request, 'adminLte/pages/main_page.html')


@login_required(login_url='/adminLte/account/login')
def about_cinema(request):
    return render(request, 'adminLte/pages/about_cinema.html')


@login_required(login_url='/adminLte/account/login')
def cafe_bar(request):
    return render(request, 'adminLte/pages/cafe_bar.html')


@login_required(login_url='/adminLte/account/login')
def vip_room(request):
    return render(request, 'adminLte/pages/vip_room.html')


@login_required(login_url='/adminLte/account/login')
def ads(request):
    return render(request, 'adminLte/pages/ads.html')


@login_required(login_url='/adminLte/account/login')
def child_room(request):
    return render(request, 'adminLte/pages/child_room.html')


@login_required(login_url='/adminLte/account/login')
def contact(request):
    return render(request, 'adminLte/pages/contact.html')


@login_required(login_url='/adminLte/account/login')
def users_list(request):
    return render(request, 'adminLte/users/users_list.html')


@login_required(login_url='/adminLte/account/login')
def redact(request):
    return render(request, 'adminLte/users/redact.html')


@login_required(login_url='/adminLte/account/login')
def user_choose(request):
    return render(request, 'adminLte/mailing/user_choose.html')


@login_required(login_url='/adminLte/account/login')
def mailing(request):
    return render(request, 'adminLte/mailing/mailing.html')
