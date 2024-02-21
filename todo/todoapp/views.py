from django.shortcuts import render, redirect
from .models import TodoItem
# Create your views here.


def new_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc', '')
        newTask = TodoItem.objects.create(title=title, description=desc)
        return redirect('display')
    return render(request, 'new_task.html')


def display(request):
    tasks = TodoItem.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def remove(request, task_id):
    task = TodoItem.objects.get(id=task_id)
    task.delete()
    return redirect('display')
