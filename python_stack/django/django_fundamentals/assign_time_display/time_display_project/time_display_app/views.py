from django.shortcuts import render , HttpResponse , redirect
from time import time, gmtime,strftime
# Create your views here.
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M:%S %p  ", gmtime()),
    }
    print(context['time'])
    return render(request,'index.html',context)


def time_display(request):
    return redirect(index)
