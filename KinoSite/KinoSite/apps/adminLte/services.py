from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


import os
import uuid

from django.db import models
from . import models as c_models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


def delete_file_with_path(path: str):
    if os.path.isfile(path):
        os.remove(path)


def delete_file_with_instance(instance):
    if instance:
        delete_file_with_path(instance.path)


def form_template(request, instance: models.Model, form_class, redirect_url_name: str, template_file_name: str, context=None):
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
