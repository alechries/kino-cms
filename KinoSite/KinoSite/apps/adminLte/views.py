from .models import Film
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FilmForm
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import DeleteView, CreateView, UpdateView
from django.views.decorators.csrf import csrf_protect, csrf_exempt


def index(request):
    return render(request, 'adminLte/index.html')


def banner(request):
    return render(request, 'adminLte/banner.html')


def film_edit_form_post(request):
    form = FilmForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('film_list')


def film_edit_form_get(request, pk=None):
    if pk is not None:
        film = get_object_or_404(Film, pk=pk)
        form = FilmForm(instance=film)
    else:
        form = FilmForm()

    return render(request, 'adminLte/film/film_form.html', {'form': form})


def film_edit_form(request, pk=None):
    if request.method == 'POST':
        response = film_edit_form_post(request)
    elif request.method == 'GET':
        response = film_edit_form_get(request, pk)
    else:
        response = redirect('film_list')
    return response


def film_list(request):
    film = Film.objects.all()

    return render(request, 'adminLte/film/film_list.html', {'film': film})


def film_delete(request, pk):
    film = Film.objects.filter(id=pk)
    film.delete()
    return redirect('film_list')


def cinema_list(request):
    return render(request, 'adminLte/cinema/cinema_list.html')


def cinema_page(request):
    return redirect(request, 'adminLte/cinema/cinema_page.html')


def hall_page(request):
    return render(request, 'adminLte/cinema/hall_page.html')


def news_list(request):
    return render(request, 'adminLte/news/news_list.html')


def news_page(request):
    return render(request, 'adminLte/news/news_page.html')


def promotion_list(request):
    return render(request, 'adminLte/promotion/promotion_list.html')


def promotion_page(request):
    return render(request, 'adminLte/promotion/promotion_page.html')


def pages_list(request):
    return render(request, 'adminLte/pages/pages_list.html')


def main_pages(request):
    return render(request, 'adminLte/pages/main_page.html')


def about_cinema(request):
    return render(request, 'adminLte/pages/about_cinema.html')


def cafe_bar(request):
    return render(request, 'adminLte/pages/cafe_bar.html')


def vip_room(request):
    return render(request, 'adminLte/pages/vip_room.html')


def ads(request):
    return render(request, 'adminLte/pages/ads.html')


def child_room(request):
    return render(request, 'adminLte/pages/child_room.html')


def contact(request):
    return render(request, 'adminLte/pages/contact.html')


def users_list(request):
    return render(request, 'adminLte/users/users_list.html')


def redact(request):
    return render(request, 'adminLte/users/redact.html')


def user_choose(request):
    return render(request, 'adminLte/mailing/user_choose.html')


def mailing(request):
    return render(request, 'adminLte/mailing/mailing.html')
