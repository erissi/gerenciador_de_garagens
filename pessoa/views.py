from django.shortcuts import render

from .forms import CadastrarUsuario
from .models import Pessoa


# Create your views here.

def cadastrarusuario(request):
    context = {}
    context['is_valid'] = False
    context['objeto'] = 'Usuário'
    if request.method == 'POST':
        form = CadastrarUsuario(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            pessoa = Pessoa(nome=form.cleaned_data['nome'], email=form.cleaned_data['email'], telefone=form.cleaned_data['telefone'])
            pessoa.save()
            form = CadastrarUsuario()
    else:
        form = CadastrarUsuario()
    context['form'] = form
    template_name = 'cadastro.html'
    return render(request, template_name, context)

