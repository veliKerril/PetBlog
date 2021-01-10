from django.urls import path
from . import views


urlpatterns = [
    # главная страница
    path('', views.main, name='main'),
    # страница со всеми постами по дате добавления
    path('all_posts/', views.all_posts, name='all_posts'),
    # страница непосредственно поста
    path('cur_posts/', views.posts, name='posts'),
    # страница для создание нового поста
    path('create/', views.create, name='create'),
    # страничка с регистрацией
    path('registration/', views.registration, name='registration'),
    # страница по категориям всех постов
    # тут надо передавать id категории? Вроде нет
    path('categories/', views.categories, name='categories'),
    # страница по автором всех постов
    path('authors_posts', views.authors_posts, name='authors_posts'),
    # страница с автором с его данными
    path('user', views.user, name='user'),
]

