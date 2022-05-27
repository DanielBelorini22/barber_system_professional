from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Task, TipoCorte, Corte, DURACAO_CHOICES
from .forms import TipoCorteForm, CorteForm

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
        form = TipoCorteForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()

            messages.info(request, 'Tarefa criada com sucesso!')

            return redirect('/')
    else:
        form = TipoCorteForm()
        return render(request, template_name, {'form': form})


@login_required
def edit_task(request, pk, template_name="tasks/edittask.html"):
    task = get_object_or_404(Task, pk=pk)
    form = TipoCorteForm(instance=task)

    if request.method == 'POST':
        form = TipoCorteForm(request.POST, instance=task)

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
    tipos_cortes = TipoCorte.objects.all()

    return render(request, template_name, {'tipos': tipos_cortes})


@login_required
def novo_tipo_corte(request, template_name="tipo_cortes/add_edit_tipo_corte.html"):
    if request.method != 'POST':
        form = TipoCorteForm()
        return render(request, template_name, {'form': form})

    form = TipoCorteForm(request.POST)
    if not form.is_valid():
        return render(request, template_name, {'form': form})

    corte = form.save(commit=False)
    corte.save()

    messages.success(request, 'Corte criado com sucesso!')

    return redirect('/tarefas/tipo-cortes')


@login_required
def editar_tipo_corte(request, pk, template_name="tipo_cortes/add_edit_tipo_corte.html"):
    tipo_corte = get_object_or_404(TipoCorte, pk=pk)
    form = TipoCorteForm(instance=tipo_corte)

    if request.method == 'POST':
        form = TipoCorteForm(request.POST, instance=tipo_corte)

        if form.is_valid():
            tipo_corte.save()

            messages.success(request, 'Corte editado com sucesso!')

            return redirect('/tarefas/tipo-cortes')
        else:
            return render(request, template_name, {'form': form, 'tipo_corte': tipo_corte})
    else:
        return render(request, template_name, {'form': form, 'tipo_corte': tipo_corte})


@login_required
def remover_tipo_corte(request, pk):
    tipo_corte = get_object_or_404(TipoCorte, pk=pk)
    tipo_corte.delete()

    messages.success(request, 'Tipo de corte deletado com sucesso!')

    return redirect('/tarefas/tipo-cortes')


@login_required
def cortes(request, template_name="cortes/list.html"):
    lista_cortes = Corte.objects.all()

    return render(request, template_name, {'cortes': lista_cortes})


def valida_intersecao_corte(corte: Corte):
    def get_minutos(time_str: str) -> int:
        h, m = time_str.split(':')
        return int(h) * 60 + int(m)

    duracao = list(filter(lambda x: x[0] == corte.duracao, DURACAO_CHOICES))
    duracao = duracao[0]
    duracao = duracao[1]

    fim_corte = corte.horario + datetime.timedelta(minutes=get_minutos(duracao))
    intersecoes = Corte.objects.filter(horario__gte=corte.horario, horario__lte=fim_corte)

    return bool(intersecoes.count())


@login_required
def novo_corte(request, template_name="cortes/add_edit_corte.html"):
    if request.method != 'POST':
        form = CorteForm()
        return render(request, template_name, {'form': form})

    form = CorteForm(request.POST)
    if not form.is_valid():
        return render(request, template_name, {'form': form})

    corte = form.save(commit=False)
    corte.duracao = form.fields['tipo_corte'].queryset.first().duracao

    if valida_intersecao_corte(corte):
        form.add_error('horario', 'Já existe um corte no período informado!')
        return render(request, template_name, {'form': form})

    corte.save()

    messages.success(request, 'Corte criado com sucesso!')

    return redirect('/tarefas/cortes')


@login_required
def editar_corte(request, pk, template_name="cortes/add_edit_corte.html"):
    corte = get_object_or_404(Corte, pk=pk)
    form = CorteForm(instance=corte)

    if request.method == 'POST':
        form = CorteForm(request.POST, instance=corte)

        if form.is_valid():
            corte.duracao = form.fields['tipo_corte'].queryset.first().duracao
            corte.save()

            messages.success(request, 'Corte editado com sucesso!')

            return redirect('/tarefas/cortes')
        else:
            return render(request, template_name, {'form': form, 'corte': corte})
    else:
        return render(request, template_name, {'form': form, 'corte': corte})


@login_required
def remover_corte(request, pk):
    corte = get_object_or_404(Corte, pk=pk)
    corte.delete()

    messages.success(request, 'Corte deletado com sucesso!')

    return redirect('/tarefas/cortes')
