from django.urls import path, include
from .components_public import views as public_views
from .components_admin import views as admin_views
from django.urls import path
from . import services

urlpatterns = [


    ###############
    # PUBLIC URLS #
    ###############
    path('', public_views.index, name='public_views.index'),
    path('account/cabinet', public_views.account_cabinet, name='account_cabinet'),
    path('account/login', public_views.account_login, name='account_login'),
    path('account/logout', public_views.account_logout, name='account_logout'),
    path('account/registration', public_views.account_registration, name='account_registration'),
    path('posters/films/list', public_views.posters_films_list, name='posters_films_list'),
    path('posters/films/details/<int:pk>/', public_views.posters_films_details, name='posters_films_details'),
    path('timetable/films/sessions/list', public_views.timetable_films_sessions_list, name='timetable_films_sessions_list'),
    path('timetable/reservation/<int:pk>', public_views.timetable_reservation, name='timetable_reservation'),
    path('cinema/list', public_views.cinema_list, name='cinema_list'),
    path('cinema/details/<int:pk>', public_views.cinema_details, name='cinema_details'),
    path('cinema/hall/details/<int:pk>', public_views.cinema_hall_details, name='cinema_hall_details'),
    path('promotion/list', public_views.promotion_list, name='promotion_list'),
    path('promotion/details/<int:pk>', public_views.promotion_details, name='promotion_details'),
    path('about/cinema', public_views.about_cinema, name='about_cinema'),
    path('about/news', public_views.about_news, name='about_news'),
    path('about/cafe-bar', public_views.about_cafe_bar, name='about_cafe-bar'),
    path('about/vip-hall', public_views.about_vip_hall, name='about_vip-hall'),
    path('about/advertising', public_views.about_advertising, name='about_advertising'),
    path('about/mobile-app', public_views.about_mobile_app, name='about_mobile-app'),
    path('about/contacts', public_views.about_contacts, name='about_contacts'),


    ##############
    # ADMIN URLS #
    ##############
    path('admin/', services.admin_views_proxy(admin_views.admin_index), name='admin_index'),
    path('admin/account/login', admin_views.account_login, name='admin_login'),
    path('admin/account/logout', admin_views.account_logout, name='admin_logout'),
    path('admin/banner/list', services.admin_views_proxy(admin_views.banner), name='admin_banner_list'),
    path('admin/banner/main_slide/form', services.admin_views_proxy(admin_views.main_slide_form), name='admin_main_slide_form'),
    path('admin/banner/main_slide/form/<int:pk>', services.admin_views_proxy(admin_views.main_slide_form, have_pk=True), name='admin_main_slide_edit'),
    path('admin/banner/main_slide/delete/<int:pk>', services.admin_views_proxy(admin_views.main_slide_delete, have_pk=True), name='admin_main_slide_delete'),
    path('admin/banner/news_promo_slide/form', services.admin_views_proxy(admin_views.news_promo_slide_form), name='admin_news_promo_slide_form'),
    path('admin/banner/news_promo_slide/form/<int:pk>', services.admin_views_proxy(admin_views.news_promo_slide_form, have_pk=True), name='admin_news_promo_slide_edit'),
    path('admin/banner/news_promo_slide/delete/<int:pk>', services.admin_views_proxy(admin_views.news_promo_slide_delete, have_pk=True), name='admin_news_promo_slide_delete'),
    path('admin/banner/background/form', services.admin_views_proxy(admin_views.background_banner_form), name='background_banner_form'),
    path('admin/film/list', services.admin_views_proxy(admin_views.film_list), name='admin_film_list'),
    path('admin/film/delete/<int:pk>', services.admin_views_proxy(admin_views.film_delete, have_pk=True), name='admin_film_delete'),
    path('admin/film/form', services.admin_views_proxy(admin_views.film_edit_form), name='admin_film_form'),
    path('admin/film/form/<int:pk>', services.admin_views_proxy(admin_views.film_edit_form, have_pk=True), name='admin_film_edit'),
    path('admin/film/form/session', services.admin_views_proxy(admin_views.session_form), name='admin_film_session'),
    path('admin/film/form/session/<int:pk>', services.admin_views_proxy(admin_views.session_form, have_pk=True), name='admin_film_session_edit'),
    path('admin/film/form/session/delete/<int:pk>', services.admin_views_proxy(admin_views.session_delete, have_pk=True), name='admin_film_session_delete'),
    path('admin/cinema/list', services.admin_views_proxy(admin_views.cinema_list), name='admin_cinema_list'),
    path('admin/cinema/form', services.admin_views_proxy(admin_views.cinema_form), name='admin_cinema_form'),
    path('admin/cinema/form/<int:pk>', services.admin_views_proxy(admin_views.cinema_form, have_pk=True), name='admin_cinema_edit'),
    path('admin/cinema/delete/<int:pk>', services.admin_views_proxy(admin_views.cinema_delete, have_pk=True), name='admin_cinema_delete'),
    path('admin/hall/form', services.admin_views_proxy(admin_views.hall_form), name='admin_hall_form'),
    path('admin/hall/form/<int:pk>', services.admin_views_proxy(admin_views.hall_form, have_pk=True), name='admin_hall_edit'),
    path('admin/hall/delete/<int:pk>', services.admin_views_proxy(admin_views.hall_delete, have_pk=True), name='admin_hall_delete'),
    path('admin/news/list', services.admin_views_proxy(admin_views.news_list), name='admin_news_list'),
    path('admin/news/form', services.admin_views_proxy(admin_views.news_form), name='admin_news_form'),
    path('admin/news/form/<int:pk>', services.admin_views_proxy(admin_views.news_form, have_pk=True), name='admin_news_edit'),
    path('admin/news/delete/<int:pk>', services.admin_views_proxy(admin_views.news_delete, have_pk=True), name='admin_news_delete'),
    path('admin/promotion/list', services.admin_views_proxy(admin_views.promotion_list), name='admin_promotion_list'),
    path('admin/promotion/form', services.admin_views_proxy(admin_views.promotion_form), name='admin_promotion_form'),
    path('admin/promotion/form/<int:pk>', services.admin_views_proxy(admin_views.promotion_form, have_pk=True), name='admin_promotion_edit'),
    path('admin/promotion/delete/<int:pk>', services.admin_views_proxy(admin_views.promotion_delete, have_pk=True), name='admin_promotion_delete'),
    path('admin/pages/list', services.admin_views_proxy(admin_views.pages_list), name='admin_pages_list'),
    path('admin/pages/main/info', services.admin_views_proxy(admin_views.main_pages), name='admin_main_info'),
    path('admin/pages/about/cinema', services.admin_views_proxy(admin_views.about_cinema), name='admin_about_cinema'),
    path('admin/pages/cafe/bar', services.admin_views_proxy(admin_views.cafe_bar), name='admin_cafe_bar'),
    path('admin/pages/vip/hall', services.admin_views_proxy(admin_views.vip_hall), name='admin_vip_hall'),
    path('admin/pages/ads', services.admin_views_proxy(admin_views.ads), name='admin_ads'),
    path('admin/pages/child/room', services.admin_views_proxy(admin_views.child_room), name='admin_child_room'),
    path('admin/pages/contact/list', services.admin_views_proxy(admin_views.contact_list), name='admin_contact_list'),
    path('admin/pages/contact/form', services.admin_views_proxy(admin_views.contact_form), name='admin_contact_form'),
    path('admin/pages/contact/edit/<int:pk>', services.admin_views_proxy(admin_views.contact_form, have_pk=True), name='admin_contact_edit'),
    path('admin/pages/contact/delete/<int:pk>', services.admin_views_proxy(admin_views.contact_delete, have_pk=True), name='admin_contact_delete'),
    path('admin/user/choose', services.admin_views_proxy(admin_views.user_choose), name='admin_user_choose'),
    path('admin/main/page', services.admin_views_proxy(admin_views.main_pages), name='admin_main_page'),
    path('admin/about/cinema', services.admin_views_proxy(admin_views.about_cinema), name='admin_about_cinema'),
    path('admin/users/list', services.admin_views_proxy(admin_views.users_list), name='admin_users_list'),
    path('admin/user/change_password/<int:pk>', services.admin_views_proxy(admin_views.user_change_password, have_pk=True), name='admin_user_change_password'),
    path('admin/user/form', services.admin_views_proxy(admin_views.user_form), name='admin_user_form'),
    path('admin/user/form/<int:pk>', services.admin_views_proxy(admin_views.user_form, have_pk=True), name='admin_user_edit'),
    path('admin/user/delete/<int:pk>', services.admin_views_proxy(admin_views.user_delete, have_pk=True), name='admin_user_delete'),
    path('admin/mailing/choose', services.admin_views_proxy(admin_views.user_choose), name='admin_user_choose'),
    path('admin/mailing', services.admin_views_proxy(admin_views.mailing), name='admin_mailing'),
]