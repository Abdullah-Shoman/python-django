from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)


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