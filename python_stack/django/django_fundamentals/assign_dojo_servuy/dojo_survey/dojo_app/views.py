from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def result(request):
    user_name = request.POST['your_name']
    user_location = request.POST['location']
    user_language = request.POST['language']
    user_comment = request.POST['comment']
    context = {
        'posted_name': user_name,
        'posted_location': user_location,
        'posted_language': user_language,
        'posted_comment':user_comment
    }
    return render(request,'result.html', context)