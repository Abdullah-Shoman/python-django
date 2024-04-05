from django.shortcuts import render,redirect
from . import models
from django.contrib import messages


# first view 
def index(request):
    return redirect(view_shows)
def view_shows(request):
    context = {
        'shows_table':models.Show.objects
    }
    return render (request,'view_shows.html',context)
# add form 
def add_new_show(request):
    if request.method == 'POST':
        errors = models.Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return render(request,'new_show.html')
        else:
            form_title = request.POST['title']
            form_network = request.POST['network']
            form_release_date = request.POST['release_date']
            form_description = request.POST['description']
            show = models.create_new_show(form_title,form_network,form_release_date,form_description)
            return redirect('/shows/'+str(show.id))
    return render(request,'new_show.html')
# back to show table
def go_back(request):
    return redirect(view_shows)
# show a certain show
def view_certain_show(request,show_id):
    context = {
        'id':show_id,
        'show':models.get_show(show_id)
    }
    return render(request,'view_show.html',context)
# form for edit show
def edit_show(request,show_id):
    context = {
        'show':models.get_show(show_id)
    }
    return render(request ,'edit_show.html',context)
# form update data
def update_show(request):
    if request.method =='POST':
        form_id = request.POST['show_id']
        errors = models.Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/"+str(form_id)+"/edit")
        else:
            form_id = request.POST['show_id']
            form_title = request.POST['title']
            form_network = request.POST['network']
            form_release_date = request.POST['release_date']
            form_description = request.POST['description']
            models.update_show(form_id,form_title,form_network,form_release_date,form_description)
    return redirect('/shows/'+str(form_id))
# delete data
def delete_show(request,show_id):
    models.delete_show(show_id)
    return redirect(index)