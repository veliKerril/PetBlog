from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Author, Category, Comment


# главная страница
def main(request):
    return render(request, 'posts/main.html')


# страница со всеми постами по дате добавления
def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/all_posts.html', {"posts": posts})


# страница непосредственно поста
def cur_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'posts/cur_post.html', {"post": post})


# страница по категориям всех постов
def categories(request):
    categories = Category.objects.all()
    return render(request, 'posts/categories.html', {"categories": categories})


# страница по автором всех постов
def authors_posts(request):
    authors = Author.objects.all()
    return render(request, 'posts/authors_posts.html', {"authors": authors})


# страница для создание нового поста
def create(request):
    return render(request, 'posts/create.html')


# страничка с регистрацией
def registration(request):
    return render(request, 'posts/registration.html')


# страница с авторами
def user(request):
    authors = Author.objects.all()
    return render(request, 'posts/user.html', {"authors": authors})


# Функция со всеми постами этой категории
def posts_by_categories(request, slug, category_id):
    posts = Post.objects.filter(category_id=category_id)
    return render(request, 'posts/posts_by_categories.html', {"posts": posts})


# Функция со всеми постапи этого автора
def posts_by_authors(request, slug, author_id):
    posts = Post.objects.filter(author_id=author_id)
    return render(request, 'posts/posts_by_authors.html', {"posts": posts})


# страница с автором и информации о нем
def about_user(request, slug, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'posts/about_user.html', {'author': author})
