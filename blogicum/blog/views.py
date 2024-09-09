from django.shortcuts import get_object_or_404, render

from .constants import AMOUNT_POSTS_ON_MAIN_PAGE

from .models import Category, Post


def index(request):
    """Показывает на главной странице."""
    print(Post.post_objects.all())  # Строка для отладки
    posts = Post.post_objects.all()[:AMOUNT_POSTS_ON_MAIN_PAGE]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Показывает страницы публикаций."""
    post = get_object_or_404(Post.post_objects.all(), id=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Показывает страницы категорий."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = Post.post_objects.all().filter(category=category)
    return render(
        request,
        'blog/category.html',
        {'category': category, 'post_list': posts}
    )
