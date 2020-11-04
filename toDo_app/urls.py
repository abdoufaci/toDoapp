from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_toDo', views.add_todo, name='add_toDo'),
    path('delete_toDo/<int:todo_id>', views.delete_todo, name='delete_toDo')
]