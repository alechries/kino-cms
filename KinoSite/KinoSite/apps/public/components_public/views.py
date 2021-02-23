from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .. import models, forms as g_forms, utils, services, auth
import datetime
from django.contrib.auth.forms import UserCreationForm

def index_view(request):
    now = datetime.date.today()
    full_date_now = datetime.date.today()
    background_banner = models.BackgroundBanner.get_solo()
    films_today = models.Film.objects.filter(first_night__lte=now)
    promo_banners = models.NewsPromoSlide.objects.all()
    n = models.Film.objects.all().count()
    telephone = models.MainPage.get_solo()
    first_film_now = {}
    if n > 1:
        film_now = models.Film.objects.all()[1:n]
        first_film_now = models.Film.objects.all()[0]
    elif n == 1:
        film_now = models.Film.objects.all()
        first_film_now = models.Film.objects.all()[0]
    else:
        film_now = models.Film.objects.all()
    future_film = models.Film.objects.filter(first_night__gt=now)
    return render(request, 'public/index.html', {'background_banner': background_banner,
                                                 'telephone': telephone,
                                                 'films_today': films_today,
                                                 'future_film': future_film,
                                                 'date_now': full_date_now,
                                                 'promo_banners': promo_banners,
                                                 'film_now': film_now,
                                                 'first_film_now': first_film_now,
                                                 })


def account_cabinet_view(request):
    user = request.user
    if user.is_authenticated:
        return utils.form_template(
            request=request,
            instance=user,
            form_class=g_forms.UserForm,
            redirect_url_name='account_cabinet',
            template_file_name='public/account/cabinet.html',
            context={'user_pk': user.id}
        )
    else:
        return redirect('account_login')


def account_login_view_decorator(redirect_to):
    def account_login_view(request):
        if request.method == 'POST':
            form = g_forms.LoginForm(request.POST)
            if form.is_valid():
                user = auth.EmailAuthBackend.authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect(redirect_to)
                    else:
                        _message = 'User is not active'
                else:
                    _message = 'User does not exist'
            else:
                _message = 'Data is incorrect'
        else:
            _message = 'Please, Sign in'
        return render(request, 'public/account/login.html', {'form': g_forms.LoginForm(), 'message': _message})
    return account_login_view


def account_logout_view(request):
    logout(request)
    return redirect('public_views.index')


def account_registration_view(request):
    form = g_forms.RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('public_views.index')
    return render(request, 'public/account/registration.html', context={'form': g_forms.RegisterForm()})


def user_change_password_view(request):
    form = g_forms.UserPasswordForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = request.user
        password = form.cleaned_data['password']
        services.Change.user_password(user, password)
        return redirect('account_cabinet')
    return render(request, 'public/account/change_password.html', context={'form': form})


def posters_films_list_view(request):
    films = models.Film.objects.all().order_by('first_night')
    background_banner = models.BackgroundBanner.get_solo()
    return render(request, 'public/posters/films_list.html', {'films': films,
                                                              'background_banner': background_banner,
                                                              })


def posters_films_details_view(request, pk):
    film = get_object_or_404(models.Film, pk=pk)
    sessions = models.FilmSession.objects.filter(film=film)

    background_banner = models.BackgroundBanner.get_solo()
    return render(request, 'public/posters/film_details.html', {'film': film,
                                                                'background_banner': background_banner,
                                                                'sessions': sessions
                                                                })


def timetable_films_sessions_list_view(request):
    return render(request, 'public/timetable/films-sessions-cinema_list.html')


def timetable_reservation_view(request, pk):
    return render(request, 'public/timetable/reservation.html')


def cinema_list_view(request):
    cinemas = models.Cinema.objects.all()
    background_banner = models.BackgroundBanner.get_solo()
    return render(request, 'public/cinema/cinema_list.html',{'cinemas': cinemas,
                                                             'background_banner': background_banner,
                                                             })


def cinema_details_view(request, pk):
    cinema = get_object_or_404(models.Cinema, pk=pk)
    background_banner = models.BackgroundBanner.get_solo()
    return render(request, 'public/cinema/details.html', {'cinema': cinema,
                                                          'background_banner': background_banner,
                                                          })


def cinema_hall_details_view(request, pk):
    return render(request, 'public/cinema/hall_details.html')


def promotion_list_view(request):
    promo_banners = models.NewsPromoSlide.objects.all()
    promotions = models.Promotion.objects.filter(promo_status='ON')
    background_banner = models.BackgroundBanner.get_solo()
    return render(request, 'public/promotion/promotions_list.html', {'promotions': promotions,
                                                                     'promo_banners': promo_banners,
                                                                     'background_banner': background_banner})


def promotion_details_view(request, pk):
    promotion = models.Promotion.objects.filter(id=pk)
    promo_banners = models.NewsPromoSlide.objects.all()
    background_banner = models.BackgroundBanner.get_solo()
    return render(request, 'public/promotion/promotion.html',{'promotion': promotion,
                                                              'background_banner': background_banner,
                                                              'promo_banners': promo_banners,
                                                              })


def about_cinema_view(request):
    background_banner = models.BackgroundBanner.get_solo()
    cinema = models.AboutCinema.get_solo()
    return render(request, 'public/about/cinema.html', {'cinema': cinema,
                                                        'background_banner': background_banner
                                                        })


def about_news_view(request):
    background_banner = models.BackgroundBanner.get_solo()
    promo_banners = models.NewsPromoSlide.objects.all()
    news = models.News.objects.filter(news_status='ON')
    return render(request, 'public/about/news.html', {'background_banner': background_banner,
                                                      'promo_banners': promo_banners,
                                                      'news': news,
                                                      })


def about_cafe_bar_view(request):
    background_banner = models.BackgroundBanner.get_solo()
    cafe = models.CafeBar.get_solo()
    return render(request, 'public/about/cafe-bar.html', {'cafe': cafe,
                                                          'background_banner': background_banner,
                                                          })


def about_vip_hall_view(request):
    background_banner = models.BackgroundBanner.get_solo()
    vip_hall = models.VipHall.get_solo()
    return render(request, 'public/about/vip-hall.html', {'vip_hall': vip_hall,
                                                          'background_banner': background_banner,
                                                          })


def about_advertising_view(request):
    background_banner = models.BackgroundBanner.get_solo()
    adv = models.Advertising.get_solo()
    return render(request, 'public/about/advertising.html', {'background_banner': background_banner,
                                                             'adv': adv,
                                                             })


def about_mobile_app_view(request):
    app = models.MobileApp.get_solo()
    background_banner = models.BackgroundBanner.get_solo()
    return render(request, 'public/about/mobile-app.html', {'background_banner': background_banner,
                                                            'app': app})


def about_child_room_view(request):
    background_banner = models.BackgroundBanner.get_solo()
    child_room = models.ChildRoom.get_solo()
    return render(request, 'public/about/child-room.html', {'child_room': child_room,
                                                            'background_banner': background_banner,
                                                             })


def about_contacts_view(request):
    background_banner = models.BackgroundBanner.get_solo()
    contacts = models.Contact.objects.all()
    return render(request, 'public/about/contacts.html', {'background_banner': background_banner,
                                                          'contacts': contacts,
                                                          })