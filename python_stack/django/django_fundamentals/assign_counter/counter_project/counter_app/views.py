from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
        request.session['counter2'] = 0
        request.session['flag'] = True
    else:
        request.session['counter'] +=1
        if request.session['flag'] == True:
            request.session['counter2'] += 1 
    request.session['flag'] = True
    return render(request , 'index.html')

def destroy(request):
    del request.session['counter']
    return redirect(index)


def add2(request):
    request.session['counter']+=1
    request.session['flag'] = False
    return redirect(index)

def user_increment(request):
    value = request.POST['increment']
    request.session['counter'] = request.session['counter'] + int(value) - 1 
    request.session['flag'] = False
    return redirect(index)