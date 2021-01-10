from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'posts/main.html')


def posts(request):
    return HttpResponse("Здесь будет непосредственно пост")


def all_posts(request):
    return HttpResponse("Здесь будет список всех постов по времени добавления")


def create(request):
    return HttpResponse("А это страничка для добавления поста")


def registration(request):
    return HttpResponse("Здесь пользователи смогут регистрироваться")


def categories(request):
    return HttpResponse("Тут будет список всех категорий")


def authors_posts(request):
    return HttpResponse("А тут будет список всех авторов и его постов")


def user(request):
    return HttpResponse("Здесь будет информация о пользователе")
