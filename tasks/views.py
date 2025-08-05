from django.shortcuts import render, redirect
from . models import Task
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from tasks.forms import TaskForm
# Create your views here.

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_create.html', {'form': form})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_update.html', {'form':form, 'task':task})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_delete.html', {'task': task})

    
    
