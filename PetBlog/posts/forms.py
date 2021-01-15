from django import forms
from .models import Post, Author, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['heading', 'text', 'category', 'author']

        labels = {
            'heading': 'Заголовок',
            'text': 'Текст поста',
            'category': 'Категория',
            'author': "Автор"
        }
