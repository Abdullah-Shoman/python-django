from django.urls import path
from . import views


urlpatterns = [
    path('' , views.index),
    path('process_money',views.process_money),
    path('destroy_session',views.destroy_session),
    path('farm',views.farm),
    path('cave',views.cave),
    path('house',views.house),
    path('quest',views.quest)
]
