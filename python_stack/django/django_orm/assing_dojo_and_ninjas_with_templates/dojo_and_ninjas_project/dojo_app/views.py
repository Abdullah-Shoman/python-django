from django.shortcuts import render , redirect
from . import models
# Create your views here.
def index(request):
    # here pass the main function for the html for each table 
    context = {
        'dojo': models.Dojo.objects,
        'ninja': models.Ninja.objects
    }
    return render(request,'index.html',context)

# route to create a new dojo and return to main route
def create_dojo(request):
    # check if the form is a post 
    if request.method == 'POST':
        models.create_dojo(request)
    return redirect('/')

# route to create a new ninja and return to main route
def create_ninja(request):
    # check id the form is a post
    if request.method == 'POST':
        models.create_ninja(request)
    return redirect('/')

def delete_dojo(request):
    # check if the form is post
    if request.method == 'POST':
        models.delete_dojo(request)
    return redirect('/')

