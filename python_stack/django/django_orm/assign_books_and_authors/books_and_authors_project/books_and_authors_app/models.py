from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    notes = models.TextField()


class Book(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    authors = models.ManyToManyField(Author,related_name= 'books')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

