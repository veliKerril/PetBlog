from django.db import models
from  django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    slug = models.CharField(max_length=40)
    about_yourself = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class Comment(models.Model):
    text = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    vote = models.IntegerField(default=0)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.pk)


class Post(models.Model):
    heading = models.CharField(max_length=40)
    text = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    vote = models.IntegerField(default=0, editable=False)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.heading
