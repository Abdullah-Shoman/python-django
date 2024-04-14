from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('main_page',views.main_page),
    path('register',views.registration_user),
    path('login',views.login_user),
    path('logout',views.logout_user),
    path('post_message',views.post_message),
    path('post_comment',views.post_comment)
]