from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request, 'my_toDo/toDoApp.html', {
        'todo_items':todo_items
    })


def add_todo(request):
    request.method
    current_date = timezone.now()
    todo = request.POST.get('todo')
    created_obj = Todo.objects.create(added_date= current_date,text=todo)
    lenght_of_todos = Todo.objects.all().count()

    return HttpResponseRedirect('/')


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')