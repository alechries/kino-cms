from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='public_views.index'),
    path('/account/cabinet', views.account_cabinet, name='account_cabinet'),
    path('/account/login', views.account_login, name='account_login'),
    path('/account/logout', views.account_logout, name='account_logout'),
    path('/account/registration', views.account_registration, name='account_registration'),
    path('/posters/films/list', views.posters_films_list, name='posters_films_list'),
    path('/posters/films/details/<int:pk>', views.posters_films_details, name='posters_films_details'),
    path('/soon', views.soon_list, name='soon'),
    path('/timetable/films/sessions/list', views.timetable_films_sessions_list, name='timetable_films_sessions_list'),
    path('/timetable/reservation/<int:pk>', views.timetable_reservation, name='timetable_reservation'),
    path('/cinema/list', views.cinema_list, name='cinema_list'),
    path('/cinema/details/<int:pk>', views.cinema_details, name='cinema_details'),
    path('/cinema/hall/details/<int:pk>', views.cinema_hall_details, name='cinema_hall_details'),
    path('/promotion/list', views.promotion_list, name='promotion_list'),
    path('/promotion/details/<int:pk>', views.promotion_details, name='promotion_details'),
    path('/about/cinema', views.about_cinema, name='about_cinema'),
    path('/about/news', views.about_news, name='about_news'),
    path('/about/cafe-bar', views.about_cafe_bar, name='about_cafe-bar'),
    path('/about/vip-hall', views.about_vip_hall, name='about_vip-hall'),
    path('/about/advertising', views.about_advertising, name='about_advertising'),
    path('/about/mobile-app', views.about_mobile_app, name='about_mobile-app'),
    path('/about/contacts', views.about_contacts, name='about_contacts'),
]