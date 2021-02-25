from django.urls import path, include
from .components_public import views as public_views
from .components_admin import views as admin_views
from django.urls import path
from django.views.generic import RedirectView
from . import utils

urlpatterns = [


    ###############
    # PUBLIC URLS #
    ###############

    path('', public_views.index_view, name='public_views.index'),
    path('favico.ico', RedirectView.as_view(url='/static/public/img/logo.ico', permanent=True)),
    path('account/cabinet', public_views.account_cabinet_view, name='account_cabinet'),
    path('account/login', public_views.account_login_view_decorator(redirect_to='account_cabinet'), name='account_login'),
    path('account/logout', public_views.account_logout_view, name='account_logout'),
    path('account/register', public_views.account_registration_view, name='account_register'),
    path('account/change_password', public_views.user_change_password_view, name='account_change_password'),
    path('posters/films/list', public_views.posters_films_list_view, name='posters_films_list'),
    path('posters/films/details/<int:pk>/', public_views.posters_films_details_view, name='posters_films_details'),
    path('timetable/films/sessions/list', public_views.timetable_films_sessions_list_view, name='timetable_films_sessions_list'),
    path('timetable/reservation/<int:pk>', public_views.timetable_reservation_view, name='timetable_reservation'),
    path('cinema/list', public_views.cinema_list_view, name='cinema_list'),
    path('cinema/details/<int:pk>', public_views.cinema_details_view, name='cinema_details'),
    path('cinema/hall/details/<int:pk>', public_views.cinema_hall_details_view, name='cinema_hall_details'),
    path('promotion/list', public_views.promotion_list_view, name='promotion_list'),
    path('promotion/details/<int:pk>', public_views.promotion_details_view, name='promotion_details'),
    path('about/cinema', public_views.about_cinema_view, name='about_cinema'),
    path('about/news', public_views.about_news_view, name='about_news'),
    path('about/cafe-bar', public_views.about_cafe_bar_view, name='about_cafe-bar'),
    path('about/vip-hall', public_views.about_vip_hall_view, name='about_vip-hall'),
    path('about/advertising', public_views.about_advertising_view, name='about_advertising'),
    path('about/mobile-app', public_views.about_mobile_app_view, name='about_mobile-app'),
    path('about/contacts', public_views.about_contacts_view, name='about_contacts'),
    path('about/child_room', public_views.about_child_room_view, name='about_child_room'),


    ##############
    # ADMIN URLS #
    ##############

    path('admin/', admin_views.admin_index_view, name='admin_index'),
    path('admin/account/login', admin_views.account_login_view, name='admin_login'),
    path('admin/account/logout', admin_views.account_logout_view, name='admin_logout'),
    path('admin/banner/list', admin_views.banner_view, name='admin_banner_list'),
    path('admin/banner/main_slide/form', admin_views.main_slide_form_view, name='admin_main_slide_form'),
    path('admin/banner/main_slide/form/<int:pk>', admin_views.main_slide_form_view, name='admin_main_slide_edit'),
    path('admin/banner/main_slide/delete/<int:pk>', admin_views.main_slide_delete_view, name='admin_main_slide_delete'),
    path('admin/banner/news_promo_slide/form', admin_views.news_promo_slide_form_view, name='admin_news_promo_slide_form'),
    path('admin/banner/news_promo_slide/form/<int:pk>', admin_views.news_promo_slide_form_view, name='admin_news_promo_slide_edit'),
    path('admin/banner/news_promo_slide/delete/<int:pk>', admin_views.news_promo_slide_delete_view, name='admin_news_promo_slide_delete'),
    path('admin/banner/background/form', admin_views.background_banner_form_view, name='background_banner_form'),
    path('admin/film/list', admin_views.film_list_view, name='admin_film_list'),
    path('admin/film/delete/<int:pk>', admin_views.film_delete_view, name='admin_film_delete'),
    path('admin/film/form', admin_views.film_edit_form_view, name='admin_film_form'),
    path('admin/film/form/<int:pk>', admin_views.film_edit_form_view, name='admin_film_edit'),
    path('admin/film/form/session', admin_views.session_form_view, name='admin_film_session'),
    path('admin/film/form/session/<int:pk>', admin_views.session_form_view, name='admin_film_session_edit'),
    path('admin/film/form/session/delete/<int:pk>', admin_views.session_delete_view, name='admin_film_session_delete'),
    path('admin/cinema/list', admin_views.cinema_list_view, name='admin_cinema_list'),
    path('admin/cinema/form', admin_views.cinema_form_view, name='admin_cinema_form'),
    path('admin/cinema/form/<int:pk>', admin_views.cinema_form_view, name='admin_cinema_edit'),
    path('admin/cinema/delete/<int:pk>', admin_views.cinema_delete_view, name='admin_cinema_delete'),
    path('admin/hall/form', admin_views.hall_form_view, name='admin_hall_form'),
    path('admin/hall/form/<int:pk>', admin_views.hall_form_view, name='admin_hall_edit'),
    path('admin/hall/delete/<int:pk>', admin_views.hall_delete_view, name='admin_hall_delete'),
    path('admin/news/list', admin_views.news_list_view, name='admin_news_list'),
    path('admin/news/form', admin_views.news_form_view, name='admin_news_form'),
    path('admin/news/form/<int:pk>', admin_views.news_form_view, name='admin_news_edit'),
    path('admin/news/delete/<int:pk>', admin_views.news_delete_view, name='admin_news_delete'),
    path('admin/promotion/list', admin_views.promotion_list_view, name='admin_promotion_list'),
    path('admin/promotion/form', admin_views.promotion_form_view, name='admin_promotion_form'),
    path('admin/promotion/form/<int:pk>', admin_views.promotion_form_view, name='admin_promotion_edit'),
    path('admin/promotion/delete/<int:pk>', admin_views.promotion_delete_view, name='admin_promotion_delete'),
    path('admin/pages/list', admin_views.pages_list_view, name='admin_pages_list'),
    path('admin/pages/main/info', admin_views.main_pages_view, name='admin_main_info'),
    path('admin/pages/about/cinema', admin_views.about_cinema_view, name='admin_about_cinema'),
    path('admin/pages/cafe/bar', admin_views.cafe_bar_view, name='admin_cafe_bar'),
    path('admin/pages/vip/hall', admin_views.vip_hall_view, name='admin_vip_hall'),
    path('admin/pages/ads', admin_views.ads_view, name='admin_ads'),
    path('admin/pages/child/room', admin_views.child_room_view, name='admin_child_room'),
    path('admin/pages/mobile/app', admin_views.mobile_app_view, name='admin_mobile_app'),
    path('admin/pages/contact/list', admin_views.contact_list_view, name='admin_contact_list'),
    path('admin/pages/contact/form', admin_views.contact_form_view, name='admin_contact_form'),
    path('admin/pages/contact/edit/<int:pk>', admin_views.contact_form_view, name='admin_contact_edit'),
    path('admin/pages/contact/delete/<int:pk>', admin_views.contact_delete_view, name='admin_contact_delete'),
    path('admin/user/choose', admin_views.user_choose_view, name='admin_user_choose'),
    path('admin/main/page', admin_views.main_pages_view, name='admin_main_page'),
    path('admin/pages/about_cinema', admin_views.about_cinema_view, name='admin_about_cinema'),
    path('admin/users/list', admin_views.users_list_view, name='admin_users_list'),
    path('admin/user/change_password/<int:pk>', admin_views.user_change_password_view, name='admin_user_change_password'),
    path('admin/user/form', admin_views.user_form_view, name='admin_user_form'),
    path('admin/user/search/', admin_views.user_search_view, name='admin_user_search'),
    path('admin/user/form/<int:pk>', admin_views.user_form_view, name='admin_user_edit'),
    path('admin/user/delete/<int:pk>', admin_views.user_delete_view, name='admin_user_delete'),
    path('admin/mailing/choose', admin_views.user_choose_view, name='admin_user_choose'),
    path('admin/mailing', admin_views.mailing_view, name='admin_mailing'),
    path('admin/seo/form/<int:pk>', admin_views.seo_form_view_decorator('admin_index'), name='admin_seo'),
]