from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name  = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def add_user(user_first_name,user_last_name,user_email,user_age):
    User.objects.create(first_name = user_first_name , last_name = user_last_name,
                        email = user_email,age = user_age)
    