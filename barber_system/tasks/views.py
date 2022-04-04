from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm

import datetime


# Create your views here.

@login_required
def taskList(request, template_name="tasks/list.html"):
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)

    elif filter:
        tasks = Task.objects.filter(done=filter, user=request.user)

    else:
        tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(tasks_list, 5)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)

    return render(request, template_name, {'tasks': tasks})


@login_required
def taskView(request, pk, template_name="tasks/task.html"):
    task = get_object_or_404(Task, pk=pk)
    return render(request, template_name, {'task': task})


@login_required
def newTask(request, template_name="tasks/addtask.html"):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()

            messages.info(request, 'Tarefa criada com sucesso!')

            return redirect('/')
    else:
        form = TaskForm()
        return render(request, template_name, {'form': form})


@login_required
def editTask(request, pk, template_name="tasks/edittask.html"):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task.save()

            messages.info(request, 'Tarefa editada com sucesso!')

            return redirect('/')
        else:
            return render(request, template_name, {'form': form, 'task': task})
    else:
        return render(request, template_name, {'form': form, 'task': task})


@login_required
def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso!')

    return redirect('/')


@login_required
def changeStatus(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if task.done == 'doing':
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()

    if task.done == 'done':
        messages.info(request, 'Tarefa concluída com sucesso!')

    if task.done == 'doing':
        messages.info(request, 'Tarefa alterada para "A fazer" com sucesso!')

    return redirect('/')


def helloWorld(request):
    return HttpResponse('Hello World!')


def yourName(request, name, template_name="tasks/yourname.html"):
    return render(request, template_name, {'name': name})


@login_required
def dashBoard(request, template_name="tasks/dashboard.html"):
    tasksDoneRecently = Task.objects.filter(done='done', updated_at__gt=datetime.datetime.now() - datetime.timedelta(days=30),
                                            user=request.user).count()
    tasksDone = Task.objects.filter(done='done', user=request.user).count()
    tasksDoing = Task.objects.filter(done='doing', user=request.user).count()
    return render(request, template_name, {'tasksDoneRecently': tasksDoneRecently, 'tasksDone': tasksDone, 'tasksDoing': tasksDoing})
