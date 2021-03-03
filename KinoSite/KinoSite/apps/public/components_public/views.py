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
    telephone = models.MainPage.get_solo()
    future_film = models.Film.objects.filter(first_night__gt=now)
    n =models.Film.objects.all().count()
    if n <= 6:
        films = models.Film.objects.all()
    else:
        films = models.Film.objects.all()[:6]
    link = models.MobileApp.get_solo()
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    return render(request, 'public/index.html', {'background_banner': background_banner,
                                                 'telephone': telephone,
                                                 'films_today': films_today,
                                                 'future_film': future_film,
                                                 'date_now': full_date_now,
                                                 'promo_banners': promo_banners,
                                                 'link': link,
                                                 'films':films,
                                                 'ads':ads,
                                                 })


def account_cabinet_view(request):
    link = models.MobileApp.get_solo()
    user = request.user
    background_banner = models.BackgroundBanner.get_solo()
    if user.is_authenticated:
        return utils.form_template(
            request=request,
            instance=user,
            form_class=g_forms.UserForm,
            redirect_url_name='account_cabinet',
            template_file_name='public/account/cabinet.html',
            context={'user_pk': user.id,
                     'background_banner': background_banner,
                     'link': link}
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
        return render(request, 'public/account/login.html', {'form': g_forms.LoginForm(), 'message': _message,
                                                             'background_banner': models.BackgroundBanner.get_solo()})
    return account_login_view


def account_logout_view(request):
    logout(request)
    return redirect('public_views.index')


def account_registration_view(request):
    link = models.MobileApp.get_solo()
    form = g_forms.RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('public_views.index')
    return render(request, 'public/account/registration.html', context={'form': g_forms.RegisterForm(),
                                                                        'link': link})


def user_change_password_view(request):
    form = g_forms.UserPasswordForm(request.POST or None)
    link = models.MobileApp.get_solo()
    if request.method == 'POST' and form.is_valid():
        user = request.user
        password = form.cleaned_data['password']
        services.Change.user_password(user, password)
        return redirect('account_cabinet')
    return render(request, 'public/account/change_password.html', context={'form': form,
                                                                           'link': link})


def posters_films_list_view(request):
    link = models.MobileApp.get_solo()
    films = models.Film.objects.all().order_by('first_night')
    background_banner = models.BackgroundBanner.get_solo()
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    return render(request, 'public/posters/films_list.html', {'films': films,
                                                              'background_banner': background_banner,
                                                              'link': link,
                                                              'ads': ads,
                                                              })


def posters_films_details_view(request, pk):
    link = models.MobileApp.get_solo()
    film = get_object_or_404(models.Film, pk=pk)
    sessions = models.FilmSession.objects.filter(film=film)
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    background_banner = models.BackgroundBanner.get_solo()
    return render(request, 'public/posters/film_details.html', {'film': film,
                                                                'background_banner': background_banner,
                                                                'sessions': sessions,
                                                                'link': link,
                                                                'ads': ads
                                                                })


def timetable_films_sessions_list_view(request):
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    context = {
        'background_banner': models.BackgroundBanner.get_solo(),
        # 'sessions': models.FilmSession.objects.filter(date=datetime.date.today())
        'sessions': models.FilmSession.objects.all(),
        'ads': ads,
        'link': models.MobileApp.get_solo()
    }
    return render(request, 'public/timetable/films-sessions-list.html', context)


def timetable_reservation_view(request, pk):
    session = models.FilmSession.objects.filter(id=pk)
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    return render(request, 'public/timetable/reservation.html',{
        'session': session,
        'ads': ads,
        'background_banner': models.BackgroundBanner.get_solo(),
    })


def cinema_list_view(request):
    cinemas = models.Cinema.objects.all()
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    background_banner = models.BackgroundBanner.get_solo()
    return render(request, 'public/cinema/cinema_list.html',{'cinemas': cinemas,
                                                             'background_banner': background_banner,
                                                             'link': models.MobileApp.get_solo(),
                                                             'ads': ads,
                                                             })


def cinema_details_view(request, pk):
    cinema = get_object_or_404(models.Cinema, pk=pk)
    background_banner = models.BackgroundBanner.get_solo()
    cinema_hall = models.CinemaHall.objects.filter(cinema=cinema)
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    return render(request, 'public/cinema/details.html', {'cinema': cinema,
                                                          'background_banner': background_banner,
                                                          'cinema_hall': cinema_hall,
                                                          'hall_count': cinema_hall.count(),
                                                          'link': models.MobileApp.get_solo(),
                                                          'ads': ads,
                                                          })


def cinema_hall_details_view(request, pk):
    hall = get_object_or_404(models.CinemaHall, pk=pk)
    sessions = models.FilmSession.objects.filter(hall=hall)
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    return render(request, 'public/cinema/hall_details.html', {'hall': hall,
                                                               'background_banner': models.BackgroundBanner.get_solo(),
                                                               'sessions': sessions,
                                                               'sessions_count': sessions.count(),
                                                               'ads': ads,
                                                               })


def promotion_list_view(request):
    promo_banners = models.NewsPromoSlide.objects.all()
    promotions = models.Promotion.objects.filter(promo_status='ON')
    background_banner = models.BackgroundBanner.get_solo()
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    return render(request, 'public/promotion/promotions_list.html', {'promotions': promotions,
                                                                     'promo_banners': promo_banners,
                                                                     'background_banner': background_banner,
                                                                     'link': models.MobileApp.get_solo(),
                                                                     'ads': ads,
                                                                     })


def promotion_details_view(request, pk):
    promotion = models.Promotion.objects.filter(id=pk)
    promo_banners = models.NewsPromoSlide.objects.all()
    background_banner = models.BackgroundBanner.get_solo()
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    return render(request, 'public/promotion/promotion.html',{'promotion': promotion,
                                                              'background_banner': background_banner,
                                                              'promo_banners': promo_banners,
                                                              'link': models.MobileApp.get_solo(),
                                                              'ads': ads,
                                                              })


def about_cinema_view(request):
    background_banner = models.BackgroundBanner.get_solo()
    cinema = {}
    row = models.AboutCinema.get_solo()
    if row.cinema_description:
        cinema = row
    return render(request, 'public/about/cinema.html', {'cinema': cinema,
                                                        'background_banner': background_banner,
                                                        'link': models.MobileApp.get_solo()
                                                        })


def about_news_view(request):
    background_banner = models.BackgroundBanner.get_solo()
    promo_banners = models.NewsPromoSlide.objects.all()
    news = models.News.objects.filter(news_status='ON')
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    return render(request, 'public/about/news.html', {'background_banner': background_banner,
                                                      'promo_banners': promo_banners,
                                                      'news': news,
                                                      'link': models.MobileApp.get_solo(),
                                                      'ads': ads
                                                      })


def about_cafe_bar_view(request):
    background_banner = models.BackgroundBanner.get_solo()
    cafe = models.CafeBar.get_solo()
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    return render(request, 'public/about/cafe-bar.html', {'cafe': cafe,
                                                          'background_banner': background_banner,
                                                          'link': models.MobileApp.get_solo(),
                                                          'ads': ads,
                                                          })


def about_vip_hall_view(request):
    background_banner = models.BackgroundBanner.get_solo()
    vip_hall = models.VipHall.get_solo()
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    return render(request, 'public/about/vip-hall.html', {'vip_hall': vip_hall,
                                                          'background_banner': background_banner,
                                                          'link': models.MobileApp.get_solo(),
                                                          'ads': ads,
                                                          })


def about_advertising_view(request):
    background_banner = models.BackgroundBanner.get_solo()
    adv = models.Advertising.get_solo()
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    return render(request, 'public/about/advertising.html', {'background_banner': background_banner,
                                                             'adv': adv,
                                                             'link': models.MobileApp.get_solo(),
                                                             'ads': ads,
                                                             })


def about_mobile_app_view(request):
    app = models.MobileApp.get_solo()
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    background_banner = models.BackgroundBanner.get_solo()
    return render(request, 'public/about/mobile-app.html', {'background_banner': background_banner,
                                                            'app': app,
                                                            'link': models.MobileApp.get_solo(),
                                                            'ads': ads
                                                            })


def about_child_room_view(request):
    background_banner = models.BackgroundBanner.get_solo()
    child_room = models.ChildRoom.get_solo()
    ads = {}
    row = models.ContextualAdvertising.get_solo()
    if row.link:
        ads = row
    return render(request, 'public/about/child-room.html', {'child_room': child_room,
                                                            'background_banner': background_banner,
                                                            'link': models.MobileApp.get_solo(),
                                                            'ads': ads,
                                                             })


def about_contacts_view(request):
    contacts = {}
    background_banner = models.BackgroundBanner.get_solo()
    row = models.Contact.objects.filter(status='ON')
    if row :
        contacts = row
    row_ads = models.ContextualAdvertising.get_solo()
    if row_ads.link:
        ads = row_ads
    return render(request, 'public/about/contacts.html', {'background_banner': background_banner,
                                                          'contacts': contacts,
                                                          'link': models.MobileApp.get_solo(),
                                                          'ads': ads
                                                          })