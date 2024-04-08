from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('add_course',views.add_course),
    path('course/delete/<int:course_id>',views.delete_course),
    path('<int:course_id>',views.destroy_course),
    path('comments/<int:course_id>',views.show_comments),
    path('comments/<int:course_id>/add_comment',views.add_course_comment)
]