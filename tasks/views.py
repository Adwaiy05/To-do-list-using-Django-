from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def list_tasks(request):
    tasks = Task.objects.all().order_by('-created_at')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:list_tasks')
        
    return render(request, 'task_list.html', {'tasks': tasks,'form' : form})

def toggle_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.completed = not task.completed 
        task.save()
    return redirect('tasks:list_tasks')  

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:list_tasks')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form,'task': task})

def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
    return redirect('tasks:list_tasks')