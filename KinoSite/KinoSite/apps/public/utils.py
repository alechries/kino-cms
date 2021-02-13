from django.shortcuts import render, redirect
from django.db import models as django_models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os


def delete_file_with_path(path: str):
    if os.path.isfile(path):
        os.remove(path)


def delete_file_with_instance(instance):
    if instance:
        delete_file_with_path(instance.path)


def form_template(request, instance: django_models.Model, form_class, redirect_url_name: str, template_file_name: str, context=None, media_context=None):
    if context is None:
        context = {}
    form = form_class(request.POST or None, request.FILES or None, instance=instance or None)
    if media_context is not None:
        context.update(media_context)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(redirect_url_name)
    context['form'] = form
    return render(request, template_file_name, context)


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