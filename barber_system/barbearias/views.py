from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from .models import *


# Create your views here.

def listar_barbearia(request, template_name='barbearia_list.html'):
    query = request.GET.get('busca', '')
    page = request.GET.get('page', '')
    ordenar = request.GET.get('ordenar', '')
    if query:
        barbearia = Barbearia.objects.filter(nome_fantasia__icontains=query)
    else:
        try:
            if ordenar:
                barbearia = Barbearia.objects.all().order_by(ordenar)
            else:
                barbearia = Barbearia.objects.all()
            barbearia = Paginator(barbearia, 2)
            barbearia = barbearia.page(page)
        except PageNotAnInteger:
            barbearia = barbearia.page(1)
        except EmptyPage:
            barbearia = paginator.page(paginator.num_pages)
    barbearias = {'lista': barbearia}
    return render(request, template_name, barbearias)


def perfil_barbearia(request, pk, template_name="perfil_barbearia.html"):
    barbearia = get_object_or_404(Barbearia, pk=pk)
    cortes = get_object_or_404(CortesCabelo, pk=pk)
    return render(request, template_name, {'barbearia': barbearia, 'cortes': cortes})


def home(request, template_name="home.html"):
    return render(request, template_name)
