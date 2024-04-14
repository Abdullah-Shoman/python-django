from django.shortcuts import render,redirect
from . import models
from django.contrib import messages
# Create your views here.
# main route 
def index(request):
    return render(request,'login_and_registration_page.html')

# route save the session for success loging, can get it through url
def main_page(request):
    if 'user_id' in request.session:
        context = {
            'user': models.User.objects.get(id = request.session['user_id']),
            'message' : models.Message.objects,
            'comment' : models.Comment.objects
        }
        return render(request,'coding_dojo_wall.html',context)
    return redirect(index)

# registration form , handle the method and validation and create user in DB
def registration_user(request):
    if request.method == 'POST':
        register_error = models.User.objects. basic_validator_register(request.POST)
        if len(register_error) > 0:
            for key, value in register_error.items():
                messages.error(request, value)
            return render(request,'login_and_registration_page.html')
        models.create_new_user(request.POST)
    return redirect(main_page)

# login form , handle the method and validation 
def login_user(request):
    if request.method == 'POST':
        login_errors = models.User.objects.basic_validator_login(request)
        if len(login_errors) > 0:
            for key, vlaue in login_errors.items():
                messages.error(request,vlaue)
            return render(request,'login_and_registration_page.html')
    return redirect(main_page)

# logout route, delete the session of the user
def logout_user(request):
    del request.session['user_id']
    return redirect(index)
#  ----------------       -----------------------         ------------------
#
def post_message(request):
    if request.method == 'POST':
        models.created_post_message(request.POST,request.session['user_id'])
    return redirect(main_page)

def post_comment(request):
    if request.method == 'POST':
        models.create_message_comment(request.POST,request.session['user_id'])
    return redirect(main_page)