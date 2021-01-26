from .models import Film
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FilmForm, LoginForm, NewsForm, UserForm
from . import models, forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


ADMIN_LOGIN_REDIRECT_URL = '/adminLte/account/login'


def content_page(request, posts_key, posts, limit: int, template: str):
    paginator = Paginator(posts, limit)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, template, {posts_key: posts, 'page': page})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def admin_index(request):
    return render(request, 'adminLte/index.html')


def account_login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
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
    return render(request, 'adminLte/account/login.html', {'form': forms.LoginForm(), 'message': _message})


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
    form = forms.FilmForm(request.POST or None, request.FILES or None, instance=film or None)
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
    cinema = get_object_or_404(models.Cinema, pk=pk) if pk else None
    halls = models.CinemaHall.objects.filter(cinema=cinema)
    form = forms.CinemaForm(request.POST or None, request.FILES or None, instance=cinema or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin_cinema_list')
    return render(request, 'adminLte/cinema/cinema_form.html', {'form': form, 'halls': halls})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def cinema_delete(request, pk):
    cinema = models.Cinema.objects.filter(id=pk)
    cinema.delete()
    return redirect('admin_cinema_list')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def hall_form(request, pk=None):
    cinema_hall = get_object_or_404(models.CinemaHall, pk=pk) if pk else None
    form = forms.CinemaHallForm(request.POST or None, request.FILES or None, instance=cinema_hall or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin_cinema_list')
    return render(request, 'adminLte/cinema/hall_form.html', {'form': form})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def hall_delete(request, pk):
    hall = models.CinemaHall.objects.filter(id=pk)
    hall.delete()
    return redirect('admin_cinema_list')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def news_form(request, pk=None):
    news = get_object_or_404(models.News, pk=pk) if pk else None
    form = forms.NewsForm(request.POST or None, request.FILES or None, instance=news or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin_news_list')
    return render(request, 'adminLte/news/news_form.html', {'form': form})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def news_list(request):
    news = models.News.objects.all()
    return render(request, 'adminLte/news/news_list.html', {'news': news})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def news_delete(request, pk):
    news = models.News.objects.filter(id=pk)
    news.delete()
    return redirect('admin_news_list')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def promotion_list(request):
    promotions = models.Promotion.objects.all()
    return render(request, 'adminLte/promotion/promotion_list.html', {'promotions': promotions})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def promotion_form(request, pk=None):
    promotion = get_object_or_404(models.Promotion, pk=pk) if pk else None
    form = forms.PromotionForm(request.POST or None, request.FILES or None, instance=promotion or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin_promotion_list')
    return render(request, 'adminLte/promotion/promotion_form.html', {'form': form})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def promotion_delete(request, pk):
    news = models.Promotion.objects.filter(id=pk)
    news.delete()
    return redirect('admin_promotion_list')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def pages_list(request):
    return render(request, 'adminLte/pages/pages_list.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def main_pages(request):
    solo: models.MainPage = models.MainPage.get_solo()
    form = forms.MainPageForm(request.POST or None, instance=solo or None)
    if request.method == 'POST' and form.is_valid():
        mp: models.MainPage = form.save(commit=False)
        mp.save()
        return redirect('admin_pages_list')
    return render(request, 'adminLte/pages/main_page.html', {'form': form})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def about_cinema(request):
    solo: models.AboutCinema = models.AboutCinema.get_solo()
    form = forms.AboutCinemaForm(request.POST or None, instance=solo or None)
    if request.method == 'POST' and form.is_valid():
        mp: models.AboutCinema = form.save(commit=False)
        mp.save()
        return redirect('admin_pages_list')
    return render(request, 'adminLte/pages/about_cinema.html', {'form': form})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def cafe_bar(request):
    solo: models.CafeBar = models.CafeBar.get_solo()
    form = forms.CafeBarForm(request.POST or None, instance=solo or None)
    if request.method == 'POST' and form.is_valid():
        mp: models.CafeBar = form.save(commit=False)
        mp.save()
        return redirect('admin_pages_list')
    return render(request, 'adminLte/pages/cafe_bar.html', {'form': form})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def vip_hall(request):
    solo: models.VipHall = models.VipHall.get_solo()
    form = forms.VipHallForm(request.POST or None, instance=solo or None)
    if request.method == 'POST' and form.is_valid():
        mp: models.AboutCinema = form.save(commit=False)
        mp.save()
        return redirect('admin_pages_list')
    return render(request, 'adminLte/pages/vip_room.html', {'form': form})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def ads(request):
    solo: models.Advertising = models.Advertising.get_solo()
    form = forms.AdvertisingForm(request.POST or None, instance=solo or None)
    if request.method == 'POST' and form.is_valid():
        mp: models.Advertising = form.save(commit=False)
        mp.save()
        return redirect('admin_pages_list')
    return render(request, 'adminLte/pages/ads.html', {'form': form})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def child_room(request):
    solo: models.ChildRoom = models.ChildRoom.get_solo()
    form = forms.ChildRoomForm(request.POST or None, instance=solo or None)
    if request.method == 'POST' and form.is_valid():
        mp: models.ChildRoom = form.save(commit=False)
        mp.save()
        return redirect('admin_pages_list')
    return render(request, 'adminLte/pages/child_room.html', {'form': form})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def contact_list(request):
    contacts = models.Contact.objects.all()
    return render(request, 'adminLte/pages/contact_list.html', {'contacts': contacts})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def contact_form(request, pk=None):
    contact = get_object_or_404(models.Contact, pk=pk) if pk else None
    form = forms.ContactForm(request.POST or None, request.FILES or None, instance=contact or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin_contact_list')
    return render(request, 'adminLte/pages/contact_form.html', {'form': form})


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def contact_delete(request, pk):
    contacts = models.Contact.objects.filter(id=pk)
    contacts.delete()
    return redirect('admin_page_list')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def users_list(request):
    users = models.User.objects.all()
    return content_page(request=request,
            posts_key='users',
            posts=users,
            limit=6,
            template='adminLte/users/users_list.html',
  )


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def user_form(request, pk=None):
    user = get_object_or_404(models.User, pk=pk) if pk else None
    form = UserForm(request.POST or None, instance=user or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('admin_users_list')
    return render(request, 'adminLte/users/user_form.html', {'form': form})


def user_delete(request, pk):
    user = models.User.objects.filter(id=pk)
    user.delete()
    return redirect('admin_users_list')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def user_choose(request):
    return render(request, 'adminLte/mailing/user_choose.html')


@login_required(login_url=ADMIN_LOGIN_REDIRECT_URL)
def mailing(request):
    return render(request, 'adminLte/mailing/mailing.html')