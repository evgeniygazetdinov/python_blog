from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Articles(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    articles = models.ManyToManyField(Articles)
