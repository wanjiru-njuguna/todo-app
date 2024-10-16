from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Todo

#view to display the todo list
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})
#view to add a new todo item
def add_todo_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        todo_item = Todo(name = name)
        todo_item.save()
        todos = Todo.objects.all()
        return render(request, 'todo_list_items.html', {'todos': todos})

#view to delete a todo item
def delete_todo_item(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)  # Fetch the todo item by ID
    todo.delete()  # Delete the todo item
    # todo_item = Todo.objects.get(id=todo_id)
    # todo_item.delete()
    todos = Todo.objects.all()
    return render(request, 'todo_list_items.html', {'todos': todos})
# a view to toggle the todo app
def toggle_todo_completion(request, todo_id):
    todo_item = Todo.objects.get(id=todo_id)
    todo_item.completed = not todo_item.completed
    todo_item.save()
    return render(request, 'todo_item.html', {'todo_item': todo_item})