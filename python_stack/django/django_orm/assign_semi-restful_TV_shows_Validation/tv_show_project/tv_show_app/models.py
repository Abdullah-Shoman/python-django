from django.db import models
import datetime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        error = {}
        if len(postData['title']) < 1 :
            error["title"] = "title should be at least 2 characters "
        if len(postData['network']) < 2:
            error['network'] = "Network should be at least 3 characters "
        if len(postData['description']) < 9:
            error['description'] = "Description should be at least 10 characters "
        if str(postData['release_date']) >= str(datetime.date.today()):
            error['release_date'] = "Release date should be in the past or grater by 10 "

        print(postData['release_date'])
        print(datetime.date.today())
        return error

class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    objects = ShowManager()

# create row
def create_new_show(form_title,form_network,form_release_date,form_description):
    show = Show.objects.create(title = form_title,network = form_network,release_date = form_release_date,description = form_description)
    # return show where we can access to id 
    return show
# get row
def get_show(show_id):
    show = Show.objects.get(id = show_id)
    return show
# update row
def update_show(form_id,form_title,form_network,form_release_date,form_description):
    show = Show.objects.get(id = form_id)
    show.title = form_title
    show.network = form_network
    show.release_date = form_release_date
    show.description = form_description
    show.save()
# delete row
def delete_show(show_id):
    show = get_show(show_id)
    show.delete()