from django.shortcuts import render
from django.utils.timezone import now  # Это можно заменить на собственную функцию получения текущего времени
from django.shortcuts import get_object_or_404
from .models import Post, Category


def index(request):
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=now(),  # Замена на подходящий способ получения текущего времени
        category__is_published=True
    ).order_by('-pub_date')[:5]  # Сортировка по дате публикации, ограничение до 5 записей
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        pk=id,
        is_published=True,
        pub_date__lte=now(),  # Текущая дата
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug, is_published=True)

    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=now()  # Текущая дата
    ).order_by('-pub_date')

    return render(request, 'blog/category.html',
                  {'category': category, 'posts': posts})


# from django.shortcuts import render
#
#
# posts = []
#
# displaying_id_post = {}
#
#
# def index(request):
#     reversed_posts = posts[::-1]  # Инвертируем список постов
#     return render(request, 'blog/index.html', {'posts': reversed_posts})
#
#
# def post_detail(request, id):
#     # Поиск поста по id
#     post = displaying_id_post.get(id)
#
#     # Если пост не найден, вернуть 404 страницу
#     if post is None:
#         return render(request, '404.html', status=404)
#
#     return render(request, 'blog/detail.html', {'post': post})
#
#
# def category_posts(request, category_slug):
#     context = {
#         'category_slug': category_slug,
#     }
#     return render(request, 'blog/category.html', context)
