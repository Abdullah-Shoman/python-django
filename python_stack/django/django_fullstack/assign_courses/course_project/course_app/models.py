from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self,postData):
        error = {}

        if len(postData['course_name']) < 5 :
            error['name'] = 'Course name should me grater than 5 character'
        # if len(postData['description']) < 15 :
        #     error['description'] = 'Description should be grater than 15 character'
        return error
    
class DescriptionManager(models.Manager):
    def basic_validator(self,postData):
        error = {}
        if len(postData['description']) < 15 :
            error['description'] = 'Description should be grater than 15 character'
        return error

class Course(models.Model):
    name = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Description(models.Model):
    description = models.TextField()
    course = models.OneToOneField(Course,on_delete=models.CASCADE,related_name='description',primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DescriptionManager()

class Comments(models.Model):
    course_comment = models.TextField()
    course = models.ForeignKey(Course,related_name="comments",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def create_course_and_description(form_course_name,form_description):
    new_course  = Course.objects.create(name = form_course_name)
    Description.objects.create(description = form_description , course = new_course)


def get_course_by_id(course_id):
    course = Course.objects.get(id = course_id)
    return course

def destroy_ourse(course_id):
    course = get_course_by_id(course_id)
    course.delete()


def get_course_comments(course_id):
    course = get_course_by_id(course_id)
    return course.comments

def add_course_comment(course_id,comment):
    course = Course.objects.get(id=course_id)
    Comments.objects.create(course_comment = comment , course = course)