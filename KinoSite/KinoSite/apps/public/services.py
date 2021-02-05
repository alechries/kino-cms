from django.shortcuts import render, redirect, get_object_or_404
from django.db import models as django_models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
import os
from datetime import date
from . import models


def delete_file_with_path(path: str):
    if os.path.isfile(path):
        os.remove(path)


def delete_file_with_instance(instance):
    if instance:
        delete_file_with_path(instance.path)


def form_template(request, instance: django_models.Model, form_class, redirect_url_name: str, template_file_name: str, context=None):
    if context is None:
        context = {}
    form = form_class(request.POST or None, request.FILES or None, instance=instance or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(redirect_url_name)
    context['form'] = form
    return render(request, template_file_name, context)


def content_page(request, posts_key, posts, limit: int, template: str):
    paginator = Paginator(posts, limit)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, template, {posts_key: posts, 'page': page})


def admin_views_proxy(func, have_pk=False):
    def proxy(request, pk=None):
        u = request.user
        if u.is_authenticated:
            if u.is_superuser:
                if not have_pk:
                    return func(request)
                else:
                    return func(request, pk)
            else:
                return redirect('public_index')
        else:
            return redirect('admin_login')
    return proxy


class Get:

    @staticmethod
    def model_list(model_sender):
        return model_sender.objects.all()


class Delete:

    @staticmethod
    def model_object(model_sender, pk=None):
        result = model_sender.objects.filter(id=pk)
        result.delete()


class Count:

    @staticmethod
    def cinema_count():
        return models.Cinema.objects.count()

    @staticmethod
    def cinema_hall_count():
        return models.CinemaHall.objects.count()

    @staticmethod
    def promotion_count():
        return models.Promotion.objects.count()

    @staticmethod
    def user_count():
        return models.User.objects.count()

    @staticmethod
    def news_count_gt_date(condition_date):
        return models.News.objects.filter(news_published_date__gt=condition_date).count()

    @staticmethod
    def news_count_lte_date(condition_date):
        return models.News.objects.filter(news_published_date__lte=condition_date).count()

    @staticmethod
    def film_count_gt_date(condition_date):
        return models.Film.objects.filter(first_night__gt=condition_date).count()

    @staticmethod
    def film_count_lte_date(condition_date):
        return models.Film.objects.filter(first_night__lte=condition_date).count()