from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'posts/main.html')


def posts(request):
    return render(request, 'posts/posts.html')


def all_posts(request):
    return render(request, 'posts/all_posts.html')


def create(request):
    return render(request, 'posts/create.html')


def registration(request):
    return render(request, 'posts/registration.html')


def categories(request):
    return render(request, 'posts/categories.html')


def authors_posts(request):
    return render(request, 'posts/authors_posts.html')


def user(request):
    return render(request, 'posts/user.html')
