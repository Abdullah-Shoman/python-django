from django.db import models

# Author Table 
class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    notes = models.TextField()

    # print the queryList with detill 
    def __str__(self):
        return f"<Author object: {self.first_name} ({self.id})>"

# Book Table
class Book(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    # create a relationship Author and Book many to many relation
    authors = models.ManyToManyField(Author,related_name= 'books')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# function on our DB

# get certain Book
def get_book(id):
    book  = Book.objects.get(id=id)
    return book
# add book function
def add_book(request):
    # form data from (html page)
    form_title = request.POST['title']
    form_description = request.POST['description']
    # create the data row
    Book.objects.create(title = form_title , description = form_description)
#function to get all the authors not included(exclude) the add one
def check__book_authors(id):
    book = get_book(id)
    authors = Author.objects.exclude(books = book)
    return authors
# add certain author to our book 
def add_auhtor_to_book(request):
    author_id = request.POST['author']
    book_id = request.POST['book_id']
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id = book_id)
    book.authors.add(author)
    return book_id

def delete_author_from_book(book_id,author_id):
    book1 = Book.objects.get(id = book_id)
    author = Author.objects.get(id = author_id)
    book1.authors.remove(author)

# ------------ authors page function 

def get_author(id):
    author  = Author.objects.get(id=id)
    return author

def check_authors_book(id):
    author = get_author(id)
    books = Book.objects.exclude(authors = author)
    return books

def add_new_author(request):
    # get the data from the post form 
    form_first_name = request.POST['first_name']
    form_last_name = request.POST['last_name']
    form_notes = request.POST['notes']
    # query 
    Author.objects.create(first_name = form_first_name , last_name = form_last_name , notes = form_notes)

def add_book_to_author(request):
    book_id = request.POST['book_id']
    author_id = request.POST['author_id']
    book = Book.objects.get(id = book_id)
    author = Author.objects.get(id = author_id)
    book.authors.add(author)
    return author_id

def delete_author_book(author_id,book_id):
    book1 = Book.objects.get(id = book_id)
    author = Author.objects.get(id = author_id)
    book1.authors.remove(author)