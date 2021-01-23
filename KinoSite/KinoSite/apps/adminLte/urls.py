from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_index, name='admin_index'),
    path('account/login', views.account_login, name='admin_login'),
    path('account/logout', views.account_logout, name='admin_logout'),
    path('banner/', views.banner, name='admin_banner'),
    path('film/list', views.film_list, name='admin_film_list'),
    path('film/delete/<int:pk>', views.film_delete, name='admin_film_delete'),
    path('film/form', views.film_edit_form, name='admin_film_form'),
    path('film/form/<int:pk>', views.film_edit_form, name='admin_film_edit'),
    path('cinema/list', views.cinema_list, name='admin_cinema_list'),
    path('cinema/page', views.cinema_page, name='admin_cinema_page'),
    path('hall/page', views.hall_page, name='admin_hall_page'),
    path('news/list', views.news_list, name='admin_news_list'),
    path('news/page', views.news_page, name='admin_news_page'),
    path('promotion/list', views.promotion_list, name='admin_promotion_list'),
    path('promotion/page', views.promotion_page, name='admin_promotion_page'),
    path('pages/list', views.pages_list, name='admin_pages_list'),
    path('main/page', views.main_pages, name='admin_main_page'),
    path('about/cinema', views.about_cinema, name='admin_about_cinema'),
    path('cafe/bar', views.cafe_bar, name='admin_cafe_bar'),
    path('vip/room', views.vip_room, name='admin_vip_room'),
    path('ads', views.ads, name='ads'),
    path('child/room', views.child_room, name='admin_child_room'),
    path('contact', views.contact, name='admin_contact'),
    path('user/list', views.users_list, name='admin_users_list'),
    path('user/edit', views.redact, name='admin_user_edit'),
    path('user/choose', views.user_choose, name='admin_user_choose'),
    path('mailing', views.mailing, name='admin_mailing'),

]