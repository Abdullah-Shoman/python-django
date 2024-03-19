from django.shortcuts import render,HttpResponse , redirect
from django.http import JsonResponse
# Create your views here.
def root(request):
    return redirect(index)

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect(root)

def show(request,number):
    return HttpResponse("placeholder to display blog number "+str(number))

def edit(request,number):
    return HttpResponse('placeholder to edit blog '+str(number))

def destory(request,number):
    return redirect(index)

def jason(request):
    return JsonResponse({'title':"My first Blog",
                        "content" : " this is the first blog using Django"})