from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_books),
    path('books/<int:id>',views.view_book),
    path('add_book',views.add_new_book),
    path('delete_author/<int:book_id>/<int:author_id>',views.delete_author),
    path('add_author',views.add_book_author),
    path('authors',views.authors),
    path('authors/add_new_author', views.add_new_author),
    path('authors/<int:author_id>',views.view_author),
    path('authors/add_book_to_author',views.add_author_book),
    path('delete_book/<int:author_id>/<int:book_id>',views.delete_book)
]