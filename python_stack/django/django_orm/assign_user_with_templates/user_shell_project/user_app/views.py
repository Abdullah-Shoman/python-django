from django.shortcuts import render,redirect
# from .models import User
from . import models
# Create your views here.
def index(request):
    context = {
            "all_the_users": models.User.objects.all()
        }

    return render(request , 'index.html', context)

def add_user(requesr):
    user_first_name = requesr.POST['first_name']
    user_last_name = requesr.POST['last_name']
    user_email = requesr.POST['email']
    user_age = requesr.POST['age']
    
    models.add_user(user_first_name , user_last_name , user_email , user_age)

    return redirect('/')