from django.shortcuts import render,redirect
from . import models
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activity'] = []
        request.session['value'] = 0
    
    return render(request , 'index.html')


def process_money(request):
    pass

def destroy_session(request):
    del request.session['gold']
    return redirect('/')

def farm(request):
    request.session['value'] = random.randint(10,20)
    request.session['gold']+=request.session['value']
    request.session['activity'].append("Earn " + str(request.session['value']))
    return redirect('/')

def cave(request):
    request.session['value'] = random.randint(10,20)
    request.session['gold']+=request.session['value']
    request.session['activity'].append("Earn " + str(request.session['value']))
    return redirect('/')

def house(request):
    request.session['value'] = random.randint(10,20)
    request.session['gold']+=request.session['value']
    request.session['activity'].append("Earn " + str(request.session['value']))
    return redirect('/')

def quest(request):
    request.session['value'] = random.randint(-50,50)
    request.session['gold']+=request.session['value']
    request.session['activity'].append("Earn " + str(request.session['value']))
    return redirect('/')