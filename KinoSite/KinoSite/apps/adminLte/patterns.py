from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
