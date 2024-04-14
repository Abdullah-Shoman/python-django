from django.db import models
import re
import bcrypt
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError as e
# Create your models here.
class UserManager(models.Manager):
    def basic_validator_register(self,postData):
        errors = {}
            # first name validation
        if len(postData['form_first_name']) < 2 :
            errors['first_name'] = 'First Name should be at lest 3 character'
        if not str.isalpha(postData['form_first_name']):
            errors['first_name_alpha'] = 'First Name should be only alphapet'
            # last name validaion
        if not str.isalpha(postData['form_last_name']):
            errors['last_name_alpha'] = 'Last Name shoulf be only alphapet'
        if len(postData['form_last_name']) < 2 :
            errors['last_name_alpha'] = 'Last name should be at least 3 character'
            # email Validation
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['form_email']):
            errors['email'] = 'Invalid email address!'
        #handle unique error
        try:
            user_email = postData['form_email']
            user1 = User.objects.get(email = user_email)
            errors['exsist_email'] = 'email is already uesed!!!'
        except:
            pass
            # password validation
        if  len(postData['form_password']) < 7:
            errors['password'] = 'password should be more than 8 character'
        if not postData['form_password'] == postData['form_confirm_pw']:
            errors['confirm_password'] = 'confirm password not match password'
        return errors
    
    def basic_validator_login(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData.POST['registered_email']):
            errors['email'] = 'Invalid email address!'
        try:
            user_email = postData.POST['registered_email']
            user1 = User.objects.get(email = user_email) 
            
        except:
            errors['check_email'] = 'user not registed'
        # check the passsword 
        if bcrypt.checkpw(postData.POST['registered_password'].encode(), user1.password.encode()):
            postData.session['user_id'] = user1.id
        else:
            errors['password'] = "the email is error or the password"
        return errors
# user table 
class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=70 , unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# message table
class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User,related_name='user_messages',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# comment table
class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Message , related_name='message_comments',on_delete=models.CASCADE)
    user  = models.ForeignKey(User,related_name='user_comments',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# created user
def create_new_user(postData):
    user_first_name = postData['form_first_name']
    user_last_name = postData['form_last_name']
    user_email = postData['form_email']
    user_password = postData['form_password']
    hash_password = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(first_name = user_first_name , last_name = user_last_name , email = user_email , password = hash_password)


def created_post_message(postData,userd_id):
    Message.objects.create(message = postData['post_message'] , user = User.objects.get(id = userd_id))

def create_message_comment(postData,user_id):
    Comment.objects.create(comment = postData['post_comment'], message = Message.objects.get(id = postData['message_id']) , user = User.objects.get(id = user_id) )

    
