from django.shortcuts import render

from .models import Veiculo
from .forms import CadastroVeiculo

# Create your views here.


def cadastrarveiculo(request):
    context = {}
    context['is_valid'] = False
    context['objeto'] = 'Veículo'
    if request.method == 'POST':
        form = CadastroVeiculo(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            veiculo = Veiculo(tipo=form.cleaned_data['tipo'],
                            modelo=form.cleaned_data['modelo'],
                            ano_de_fabricacao=form.cleaned_data['ano_de_fabricacao'],
                            cor=form.cleaned_data['cor']
            )
            veiculo.save()
            form = CadastroVeiculo()
    else:
        form = CadastroVeiculo()
    context['form'] = form
    template_name = 'cadastro.html'
    return render(request, template_name, context)


def cadastrar(request):
    context = {}
    context['is_valid'] = False
    context['objeto'] = 'Garagem'
    if request.method == 'POST':
        form = CadastroGaragem(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            veiculo = Veiculo(tipo=form.cleaned_data['tipo'],
                            modelo=form.cleaned_data['modelo'],
                            ano_de_fabricacao=form.cleaned_data['ano_de_fabricacao'],
                            cor=form.cleaned_data['cor']
            )
            veiculo.save()
            form = CadastroVeiculo()
    else:
        form = CadastroVeiculo()
    context['form'] = form
    template_name = 'cadastro.html'
    return render(request, template_name, context)