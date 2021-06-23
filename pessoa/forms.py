from django import forms

class CadastrarUsuario(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100, required=True)
    telefone = forms.CharField(label='Telefone', max_length=11, required=True)
    email = forms.EmailField(label='Email', required=True)