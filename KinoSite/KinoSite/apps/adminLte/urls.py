from django.urls import path
from . import views


urlpatterns = [
    path('', views.admin_index, name='admin_index'),
    path('account/login', views.account_login, name='account_login'),
    path('account/register', views.account_register, name='account_register'),
    path('banner/', views.banner, name='banner'),
    path('film/list', views.film_list, name='film_list'),
    path('film/delete/<int:pk>', views.film_delete, name='film_delete'),
    path('film/form', views.film_edit_form, name='film_form'),
    path('film/form/<int:pk>', views.film_edit_form, name='film_form_edit'),
    path('cinema_list', views.cinema_list, name='cinema_list'),
    path('cinema_page', views.cinema_page, name='cinema_page'),
    path('hall_page', views.hall_page, name='hall_page'),
    path('news_list', views.news_list, name='news_list'),
    path('news_page', views.news_page, name='news_page'),
    path('promotion_list', views.promotion_list, name='promotion_list'),
    path('promotion_page', views.promotion_page, name='promotion_page'),
    path('pages_list', views.pages_list, name='pages_list'),
    path('main_page', views.main_pages, name='main_page'),
    path('about_cinema', views.about_cinema, name='about_cinema'),
    path('cafe_bar', views.cafe_bar, name='cafe_bar'),
    path('vip_room', views.vip_room, name='vip_room'),
    path('ads', views.ads, name='ads'),
    path('child_room', views.child_room, name='child_room'),
    path('contact', views.contact, name='contact'),
    path('users_list', views.users_list, name='users_list'),
    path('redact', views.redact, name='redact'),
    path('user_choose', views.user_choose, name='user_choose'),
    path('mailing', views.mailing, name='mailing'),

]