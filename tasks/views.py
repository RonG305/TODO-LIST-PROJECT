from django.shortcuts import render, redirect
from django.http import HttpResponse


from tasks.forms import TaskForm
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/index.html', context)


def add_todo(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'tasks/add_todo.html', context)


def update_todo(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }

    return render(request, 'tasks/update.html', context)   


def delete_todo(request, pk):
    item = Task.objects.get(id=pk)
    item.delete()   

    context = {
        'item': item
    }

    return render(request, 'tasks/delete.html', context)  
    

   
    