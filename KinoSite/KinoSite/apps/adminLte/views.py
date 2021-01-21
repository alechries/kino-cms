from .models import Film
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FilmForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import DeleteView, CreateView, UpdateView
from django.views.decorators.csrf import csrf_protect, csrf_exempt


@login_required(login_url='/adminLte/login/')
def index(request):
    return render(request, 'adminLte/index.html')


def account_login(request):
    return render(request, 'adminLte/account/login.html')


@login_required(login_url='/adminLte/login/')
def banner(request):
    return render(request, 'adminLte/banner.html')


@login_required(login_url='/adminLte/login/')
def film_edit_form_post(request):
    form = FilmForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('film_list')


@login_required(login_url='/adminLte/login/')
def film_edit_form_get(request, pk=None):
    if pk is not None:
        film = get_object_or_404(Film, pk=pk)
        form = FilmForm(instance=film)
    else:
        form = FilmForm()

    return render(request, 'adminLte/film/film_form.html', {'form': form})


@login_required(login_url='/adminLte/login/')
def film_edit_form(request, pk=None):
    if request.method == 'POST':
        response = film_edit_form_post(request)
    elif request.method == 'GET':
        response = film_edit_form_get(request, pk)
    else:
        response = redirect('film_list')
    return response


@login_required(login_url='/adminLte/login/')
def film_list(request):
    film = Film.objects.all()

    return render(request, 'adminLte/film/film_list.html', {'film': film})


@login_required(login_url='/adminLte/login/')
def film_delete(request, pk):
    film = Film.objects.filter(id=pk)
    film.delete()
    return redirect('film_list')


@login_required(login_url='/adminLte/login/')
def cinema_list(request):
    return render(request, 'adminLte/cinema/cinema_list.html')


@login_required(login_url='/adminLte/login/')
def cinema_page(request):
    return redirect(request, 'adminLte/cinema/cinema_page.html')


@login_required(login_url='/adminLte/login/')
def hall_page(request):
    return render(request, 'adminLte/cinema/hall_page.html')


@login_required(login_url='/adminLte/login/')
def news_list(request):
    return render(request, 'adminLte/news/news_list.html')


@login_required(login_url='/adminLte/login/')
def news_page(request):
    return render(request, 'adminLte/news/news_page.html')


@login_required(login_url='/adminLte/login/')
def promotion_list(request):
    return render(request, 'adminLte/promotion/promotion_list.html')


@login_required(login_url='/adminLte/login/')
def promotion_page(request):
    return render(request, 'adminLte/promotion/promotion_page.html')


@login_required(login_url='/adminLte/login/')
def pages_list(request):
    return render(request, 'adminLte/pages/pages_list.html')


@login_required(login_url='/adminLte/login/')
def main_pages(request):
    return render(request, 'adminLte/pages/main_page.html')


@login_required(login_url='/adminLte/login/')
def about_cinema(request):
    return render(request, 'adminLte/pages/about_cinema.html')


@login_required(login_url='/adminLte/login/')
def cafe_bar(request):
    return render(request, 'adminLte/pages/cafe_bar.html')


@login_required(login_url='/adminLte/login/')
def vip_room(request):
    return render(request, 'adminLte/pages/vip_room.html')


@login_required(login_url='/adminLte/login/')
def ads(request):
    return render(request, 'adminLte/pages/ads.html')


@login_required(login_url='/adminLte/login/')
def child_room(request):
    return render(request, 'adminLte/pages/child_room.html')


@login_required(login_url='/adminLte/login/')
def contact(request):
    return render(request, 'adminLte/pages/contact.html')


@login_required(login_url='/adminLte/login/')
def users_list(request):
    return render(request, 'adminLte/users/users_list.html')


@login_required(login_url='/adminLte/login/')
def redact(request):
    return render(request, 'adminLte/users/redact.html')


@login_required(login_url='/adminLte/login/')
def user_choose(request):
    return render(request, 'adminLte/mailing/user_choose.html')


@login_required(login_url='/adminLte/login/')
def mailing(request):
    return render(request, 'adminLte/mailing/mailing.html')
