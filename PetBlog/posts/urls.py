from django.urls import path
from . import views


urlpatterns = [
    # главная страница
    path('', views.main, name='main'),
    # страница со всеми постами по дате добавления
    path('all_posts/', views.all_posts, name='all_posts'),
    # страница непосредственно поста
    path('cur_post/<int:post_id>/', views.cur_post, name='cur_post'),
    # страница для создание нового поста
    path('create/', views.create, name='create'),
    # страничка с регистрацией
    path('registration/', views.registration, name='registration'),
    # страница по категориям всех постов
    # тут надо передавать id категории? Вроде нет
    path('categories/', views.categories, name='categories'),
    # страница по автором всех постов
    path('authors_posts', views.authors_posts, name='authors_posts'),
    # страница с авторами
    path('user', views.user, name='user'),


    # Функция со всеми постами этой категории
    path('posts_by_categories/<int:category_id>/', views.posts_by_categories, name='posts_by_categories'),
    # Функция со всеми постапи этого автора
    path('posts_by_authors/<int:author_id>/', views.posts_by_authors, name='posts_by_authors'),
    # страница с автором и информации о нем
    path('about_user/<str:slug>/', views.about_user, name='about_user'),
]

