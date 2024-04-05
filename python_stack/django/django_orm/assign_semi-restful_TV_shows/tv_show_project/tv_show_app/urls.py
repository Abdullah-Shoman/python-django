from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('shows',views.view_shows),
    path('new',views.add_new_show),
    path('go_back',views.go_back),
    path('shows/<int:show_id>',views.view_certain_show),
    path('shows/<int:show_id>/edit',views.edit_show),
    path('<int:show_id>/edit',views.edit_show),
    path('update',views.update_show),
    path('<int:show_id>/destroy',views.delete_show)
]
