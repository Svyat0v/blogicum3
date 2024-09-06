from django.http import Http404

from django.shortcuts import render, get_object_or_404

from .models import Post, Category

from django.utils import timezone


def index(request):
    posts = (Post.objects
             .filter(
                 is_published=True,
                 pub_date__lte=timezone.now(),
                 category__is_published=True
             )
             .select_related('category')
             .order_by('-pub_date')[:5])

    return render(request, 'index.html', {'posts': posts})


def post_detail(request, pk):
    post = (Post.objects
            .select_related('category')
            .filter(
                pk=pk,
                is_published=True,
                pub_date__lte=timezone.now(),
                category__is_published=True)
            .first())

    if not post:
        raise Http404("Публикация не найдена или недоступна.")

    return render(request, 'post_detail.html', {'post': post})


def category_posts(request, category_slug):
    # Найти категорию или вернуть 404
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
        )

    # Получить публикации категории
    posts = (Post.objects
             .filter(
                 category=category,
                 is_published=True,
                 pub_date__lte=timezone.now()
             )
             .order_by('-pub_date'))

    return render(request, 'category_posts.html', 
                  {'category': category, 'posts': posts})


# from django.shortcuts import render


# posts = []

# displaying_id_post = {}


# def index(request):
#     reversed_posts = posts[::-1]  # Инвертируем список постов
#     return render(request, 'blog/index.html', {'posts': reversed_posts})


# def post_detail(request, id):
#     # Поиск поста по id
#     post = displaying_id_post.get(id)

#     # Если пост не найден, вернуть 404 страницу
#     if post is None:
#         return render(request, '404.html', status=404)

#     return render(request, 'blog/detail.html', {'post': post})


# def category_posts(request, category_slug):
#     context = {
#         'category_slug': category_slug,
#     }
#     return render(request, 'blog/category.html', context)
