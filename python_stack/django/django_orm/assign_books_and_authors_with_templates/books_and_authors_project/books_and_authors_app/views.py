from django.shortcuts import render,redirect
from . import models
# firsr view: show book table and form to add a new one
def view_books(request):
    context = {
        'book_table' : models.Book.objects
    }
    return render(request , 'index.html',context)
# second view is the action of adding new book then redirect to view book table
def add_new_book(request):
    if request.method == 'POST':
        models.add_book(request)
    return redirect(view_books)
# theird view show a certain book and form to add new authro
def view_book(request,id):
    context = {
        'book': models.get_book(id),
        'authors': models.check__book_authors(id)
    }
    return render(request,'books.html',context)
# delete author of certain book   
def delete_author(request,book_id,author_id):
    models.delete_author_from_book(book_id,author_id)
    return redirect('/books/'+str(book_id))
# add author of a certain book 
def add_book_author(request):
    if request.method == 'POST':
        id = models.add_auhtor_to_book(request)
    return redirect('/books/'+str(id))
# ------------------------------------ #
# show the Authors table and form to add a new one 
def authors(request):
    context = {
        'author_table': models.Author.objects
    }
    return render(request, 'authors.html',context)
# add a new author to author table
def add_new_author(request):
    if request.method == 'POST':
        models.add_new_author(request)

    return redirect(authors)
# view a certain author 
def view_author(request,author_id):
    context = {
        'author': models.get_author(author_id),
        'books':models.check_authors_book(author_id)
    }
    return render(request,'author.html',context)

def add_author_book(request):
    if request.method == 'POST':
        id = models.add_book_to_author(request)
    return redirect('/authors/'+str(id))

def delete_book(request,author_id,book_id):
    models.delete_author_book(author_id,book_id)
    return redirect('/authors/'+str(author_id))