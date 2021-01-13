from django.db import models


class Category(models.Model):
    name = models.CharField(),


class Author(models.Model):
    first_name = models.CharField(),
    last_name = models.CharField(),
    about_yourself = models.TextField(),
    email = models.EmailField(),
    image = models.ImageField(),


class Comment(models.Model):
    text = models.TextField(),
    date = models.DateTimeField(),
    vote = models.IntegerField(),
    author = models.ForeignKey(Author, on_delete=models.CASCADE),


class Post(models.Model):
    text = models.TextField(),
    date = models.DateTimeField(),
    vote = models.IntegerField(),
    author = models.ForeignKey(Author, on_delete=models.CASCADE),
    category = models.ForeignKey(Category, on_delete=models.CASCADE),
