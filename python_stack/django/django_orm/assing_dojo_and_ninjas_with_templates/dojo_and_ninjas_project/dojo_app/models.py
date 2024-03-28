from django.db import models

# Create your models here.

class Dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    desc = models.CharField(max_length = 255)


class Ninja(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    dojo = models.ForeignKey(Dojo, related_name = "ninjas" , on_delete = models.CASCADE)

# create a dojo 
def create_dojo(request):
    form_name = request.POST['dojo_name']
    form_city = request.POST['dojo_city']
    form_state = request.POST['dojo_state']
    form_desc = 'old dojo'
    # Query for creating 
    Dojo.objects.create(name = form_name, city = form_city , state = form_state,desc = form_desc)

def create_ninja(request):
    form_first_name = request.POST['ninja_first_name']
    form_last_name = request.POST['ninja_last_name']
    form_dojo = request.POST.get('ninja_dojo')
    dojo_obj = Dojo.objects.get(id = form_dojo)
    Ninja.objects.create(first_name = form_first_name , last_name = form_last_name , dojo = dojo_obj)

def delete_dojo(request):
    # here i used a hidden input where the name is id and value is the dojo_id
    form_id = request.POST['id']
    dojo = Dojo.objects.get(id = form_id)
    dojo.delete()

