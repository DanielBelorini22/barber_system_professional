from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import CorteForm

import datetime


# Create your views here.

@login_required
def task_list(request, template_name="tasks/list.html"):
    search = request.GET.get('search')
    filter_query = request.GET.get('filter')

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)

    elif filter_query:
        tasks = Task.objects.filter(done=filter_query, user=request.user)

    else:
        tasks_list = Task.objects.filter(user=request.user).order_by('-created_at')

        paginator = Paginator(tasks_list, 5)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)

    return render(request, template_name, {'tasks': tasks})


@login_required
def task_view(request, pk, template_name="tasks/task.html"):
    task = get_object_or_404(Task, pk=pk)
    return render(request, template_name, {'task': task})


@login_required
def new_task(request, template_name="tasks/addtask.html"):
    if request.method == 'POST':
        form = CorteForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()

            messages.info(request, 'Tarefa criada com sucesso!')

            return redirect('/')
    else:
        form = CorteForm()
        return render(request, template_name, {'form': form})


@login_required
def edit_task(request, pk, template_name="tasks/edittask.html"):
    task = get_object_or_404(Task, pk=pk)
    form = CorteForm(instance=task)

    if request.method == 'POST':
        form = CorteForm(request.POST, instance=task)

        if form.is_valid():
            task.save()

            messages.info(request, 'Tarefa editada com sucesso!')

            return redirect('/')
        else:
            return render(request, template_name, {'form': form, 'task': task})
    else:
        return render(request, template_name, {'form': form, 'task': task})


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso!')

    return redirect('/')


@login_required
def change_status(request, pk):
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


def hello_world(request):
    return HttpResponse('Hello World!')


def your_name(request, name, template_name="tasks/yourname.html"):
    return render(request, template_name, {'name': name})


@login_required
def dash_board(request, template_name="tasks/dashboard.html"):
    tasks_done_recently = Task.objects.filter(done='done',
                                              updated_at__gt=datetime.datetime.now() - datetime.timedelta(days=30),
                                              user=request.user).count()
    tasks_done = Task.objects.filter(done='done', user=request.user).count()
    tasks_doing = Task.objects.filter(done='doing', user=request.user).count()
    return render(request, template_name,
                  {'tasksDoneRecently': tasks_done_recently, 'tasksDone': tasks_done, 'tasksDoing': tasks_doing})


@login_required
def tipo_cortes(request, template_name="tipo_cortes/list.html"):
    return render(request, template_name, {'name': 'aa'})


@login_required
def novo_tipo_cortes(request, template_name="tipo_cortes/addcorte.html"):
    if request.method != 'POST':
        form = CorteForm()
        return render(request, template_name, {'form': form})

    form = CorteForm(request.POST)
    if not form.is_valid():
        return render(request, template_name, {'form': form})

    corte = form.save(commit=False)
    corte.save()

    messages.info(request, 'Corte criado com sucesso!')

    return redirect('/tarefas/cortes')
