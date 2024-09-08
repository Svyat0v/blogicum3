from django.shortcuts import render
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
from .models import Post, Category


def index(request):
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=now(),
        category__is_published=True
    ).order_by('-pub_date')[:5]
    context = {
        'posts': posts,
        'title': 'Последние публикации'
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        pk=id,
        is_published=True,
        pub_date__lte=now(),  # Текущая дата
        category__is_published=True
    )
    context = {
        'post': post,
        'title': post.title
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True)

    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=now()  # Текущая дата
    ).order_by('-pub_date')
    context = {
        'category': category,
        'posts': posts,
        'title': f'Публикации в категории {category.title}',
        'key2': category.description,
        'key3': posts.count()
    }

    return render(request, 'blog/category.html', context)
