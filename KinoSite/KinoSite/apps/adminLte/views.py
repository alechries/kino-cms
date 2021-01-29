from .models import Film
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from . import models, forms
from django.core.mail import send_mail
from . import services
from os import remove as remove_file
from datetime import date


def admin_index(request):
    date_now = date.today()
    context = {
        'films_will_count': models.Film.objects.filter(first_night__gt=date_now).count(),
        'films_was_count': models.Film.objects.filter(first_night__lt=date_now).count(),
        'cinema_count': models.Cinema.objects.count(),
        'cinema_hall_count': models.CinemaHall.objects.count(),
        'news_will_count': models.News.objects.filter(news_published_date__gt=date_now).count(),
        'news_was_count': models.News.objects.filter(news_published_date__lt=date_now).count(),
        'promo_count': models.Promotion.objects.count(),
        'user_count': models.User.objects.count(),
    }
    return render(request, 'adminLte/index.html', context)


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


def account_logout(request):
    logout(request)
    return redirect('admin_index')


def banner(request):
    return render(request, 'adminLte/banner.html')


def film_edit_form(request, pk=None):
    instance = get_object_or_404(models.Film, pk=pk) if pk else None
    return services.form_template(
        request=request,
        instance=instance,
        form_class=forms.FilmForm,
        redirect_url_name='admin_film_list',
        template_file_name='adminLte/film/film_form.html',
    )


def film_list(request):
    films = models.Film.objects.all()
    return render(request, 'adminLte/film/film_list.html', {'film': films})


def film_delete(request, pk):
    films: models.Film = models.Film.objects.filter(id=pk)
    films.delete()
    return redirect('admin_film_list')


def cinema_list(request):
    cinemas = models.Cinema.objects.all()
    return render(request, 'adminLte/cinema/cinema_list.html', {'cinemas': cinemas})


def cinema_form(request, pk=None):
    cinema = get_object_or_404(models.Cinema, pk=pk) if pk else None
    halls = models.CinemaHall.objects.filter(cinema=cinema)
    return services.form_template(
        request=request,
        instance=cinema,
        context={'halls': halls},
        form_class=forms.CinemaForm,
        redirect_url_name='admin_cinema_list',
        template_file_name='adminLte/cinema/cinema_form.html',
    )


def cinema_delete(request, pk):
    cinema = models.Cinema.objects.filter(id=pk)
    cinema.delete()
    return redirect('admin_cinema_list')


def hall_form(request, pk=None):
    cinema_hall = get_object_or_404(models.CinemaHall, pk=pk) if pk else None
    return services.form_template(
        request=request,
        instance=cinema_hall,
        form_class=forms.CinemaHallForm,
        redirect_url_name='admin_cinema_list',
        template_file_name='adminLte/cinema/hall_form.html',
    )


def hall_delete(request, pk):
    hall = models.CinemaHall.objects.filter(id=pk)
    hall.delete()
    return redirect('admin_cinema_list')


def news_form(request, pk=None):
    news = get_object_or_404(models.News, pk=pk) if pk else None
    return services.form_template(
        request=request,
        instance=news,
        form_class=forms.NewsForm,
        redirect_url_name='admin_news_list',
        template_file_name='adminLte/news/news_form.html',
    )


def news_list(request):
    news = models.News.objects.all()
    return render(request, 'adminLte/news/news_list.html', {'news': news})


def news_delete(request, pk):
    news = models.News.objects.filter(id=pk)
    news.delete()
    return redirect('admin_news_list')


def promotion_list(request):
    promotions = models.Promotion.objects.all()
    return render(request, 'adminLte/promotion/promotion_list.html', {'promotions': promotions})


def promotion_form(request, pk=None):
    promotion = get_object_or_404(models.Promotion, pk=pk) if pk else None
    return services.form_template(
        request=request,
        instance=promotion,
        form_class=forms.PromotionForm,
        redirect_url_name='admin_promotion_list',
        template_file_name='adminLte/promotion/promotion_form.html',
    )


def promotion_delete(request, pk):
    news = models.Promotion.objects.filter(id=pk)
    news.delete()
    return redirect('admin_promotion_list')


def pages_list(request):
    return render(request, 'adminLte/pages/pages_list.html')


def main_pages(request):
    solo: models.MainPage = models.MainPage.get_solo()
    return services.form_template(
        request=request,
        instance=solo,
        form_class=forms.MainPageForm,
        redirect_url_name='admin_index',
        template_file_name='adminLte/pages/main_page.html',
    )


def about_cinema(request):
    solo: models.AboutCinema = models.AboutCinema.get_solo()
    return services.form_template(
        request=request,
        instance=solo,
        form_class=forms.AboutCinemaForm,
        redirect_url_name='admin_index',
        template_file_name='adminLte/pages/about_cinema.html',
    )


def cafe_bar(request):
    solo: models.CafeBar = models.CafeBar.get_solo()
    return services.form_template(
        request=request,
        instance=solo,
        form_class=forms.CafeBarForm,
        redirect_url_name='admin_index',
        template_file_name='adminLte/pages/cafe_bar.html',
    )


def vip_hall(request):
    solo: models.VipHall = models.VipHall.get_solo()
    return services.form_template(
        request=request,
        instance=solo,
        form_class=forms.VipHallForm,
        redirect_url_name='admin_index',
        template_file_name='adminLte/pages/vip_room.html',
    )


def ads(request):
    solo: models.Advertising = models.Advertising.get_solo()
    return services.form_template(
        request=request,
        instance=solo,
        form_class=forms.AdvertisingForm,
        redirect_url_name='admin_index',
        template_file_name='adminLte/pages/ads.html',
    )


def child_room(request):
    solo: models.ChildRoom = models.ChildRoom.get_solo()
    return services.form_template(
        request=request,
        instance=solo,
        form_class=forms.ChildRoomForm,
        redirect_url_name='admin_index',
        template_file_name='adminLte/pages/child_room.html',
    )


def contact_list(request):
    contacts = models.Contact.objects.all()
    return render(request, 'adminLte/pages/contact_list.html', {'contacts': contacts})


def contact_form(request, pk=None):
    contact = get_object_or_404(models.Contact, pk=pk) if pk else None
    return services.form_template(
        request=request,
        instance=contact,
        form_class=forms.ContactForm,
        redirect_url_name='admin_index',
        template_file_name='adminLte/pages/contact_form.html',
    )


def contact_delete(request, pk):
    contacts = models.Contact.objects.filter(id=pk)
    contacts.delete()
    return redirect('admin_contact_list')


def users_list(request):
    users = models.User.objects.all()
    return services.content_page(request=request,
                                 posts_key='users',
                                 posts=users,
                                 limit=6,
                                 template='adminLte/users/users_list.html',
                                 )


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



def user_choose(request):
    return render(request, 'adminLte/mailing/user_choose.html')


def mailing(request):
    user = models.User.objects.values('email')
    for el in user:
        user_email = el['email']
        print(user_email)
        send_mail('Subject here', 'Here is the message.', 'dimadjangosendemail@gmail.com',
        [user_email])
    return render(request, 'adminLte/mailing/mailing.html')


def main_slide_form(request, pk=None):
    slide = get_object_or_404(models.MainSlide, pk=pk) if pk else None
    return services.form_template(
        request=request,
        instance=slide,
        form_class=forms.MainSlideForm,
        redirect_url_name='admin_banner_list',
        template_file_name='adminLte/users/user_form.html',
    )


def main_slide(request, pk):
    slide = models.MainSlide.objects.filter(id=pk)
    slide.delete()
    return redirect('admin_banner_list')