from django.shortcuts import render,redirect
from . import models
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'login_and_registration_page.html')

def sucess_registration(request):
    if 'user_id' in request.session:
        return render(request,'success.html')

    return redirect(index)

def registration_user(request):
    if request.method == 'POST':
        register_error = models.User.objects. basic_validator_register(request.POST)
        if len(register_error) > 0:
            for key, value in register_error.items():
                messages.error(request, value)
            return render(request,'login_and_registration_page.html')
        models.create_new_user(request.POST)
    return redirect(sucess_registration)

def login_user(request):
    if request.method == 'POST':
        login_errors = models.User.objects.basic_validator_login(request)
        if len(login_errors) > 0:
            for key, vlaue in login_errors.items():
                messages.error(request,vlaue)
            return render(request,'login_and_registration_page.html')
        print(request.session['user_id'])
        return redirect(sucess_registration)
    return redirect(sucess_registration)

def logout_user(request):
    del request.session['user_id']
    return redirect(index)