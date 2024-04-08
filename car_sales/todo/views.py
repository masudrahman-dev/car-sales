from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    form = TaskForm()

    return render(request, 'todo/task_form.html', {"form": form})


def task_update(request, pk):
    task = get_list_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        else:
            form = TaskForm(instance=task)
            return render(request, 'todo/task_list.html', {"form": form})


def task_delete(request, pk):
    pass


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {"tasks": tasks})
