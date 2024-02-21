
from django.urls import path
from . import views
# create a view with functions


urlpatterns = [
    path('', views.display, name='home'),
    path('view/', views.display, name='display'),
    path('new_task/', views.new_task, name='newTask'),
    path('delete_task/<str:task_id>', views.remove, name='deleteTask'),
]
