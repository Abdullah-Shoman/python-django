from django.shortcuts import render , redirect
from . import models
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'courses':models.Course.objects
    }
    return render(request,'index.html',context)


def add_course(request):
    context = {
        'courses':models.Course.objects
    }
    if request.method == 'POST':
        error1 = models.Course.objects.basic_validator(request.POST)
        error2 = models.Description.objects.basic_validator(request.POST)
        errors = {**error1,**error2}
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return render(request,'index.html',context)
        else:
            form_course_name = request.POST['course_name']
            form_description = request.POST['description']
            models.create_course_and_description(form_course_name,form_description)
            return redirect(index)
    return render(request , 'index.html' , context)

def delete_course(request,course_id):
    context = {
        'course':models.getCourseById(course_id)
    }
    return render(request,'delete_course.html',context)

def destroy_course(request,course_id):
    models.destroy_course(course_id)
    return redirect('/')

def show_comments(request,course_id):
    context = {
        'course': models.get_course_comments(course_id),
        'course_id':course_id
    }
    return render(request,'course_comments.html',context)

def add_course_comment(request,course_id):
    if request.method == 'POST':
        comment = request.POST['comment']
        models.add_course_comment(course_id,comment)
    return redirect('/comments/'+str(course_id))