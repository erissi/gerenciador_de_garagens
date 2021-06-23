from django.db import models

# Create your models here.
from ..pessoa.models import Pessoa


class GerenciadorVeiculo(models.Manager):

    def lista_veiculos(self):
        return self.get_queryset()

    def lista_motos(self):
        return self.get_queryset().filter(tipo__icontains='Moto')

    def lista_carros(self):
        return self.get_queryset().filter(tipo__icontains='Carro')

    def retorna_ano_cor(self, id):
        veiculo = self.get_queryset().filter(id)
        if veiculo.tipo == 'Carro':
            return veiculo.ano_de_fabricacao, veiculo.cor
        else:
            return veiculo.ano_de_fabricacao, veiculo.modelo


    def lista_veiculos_por_cor(self, cor):
        return self.get_queryset().filter(cor__icontains=cor)


    def lista_veiculos_por_ano(self, ano):
        return self.get_queryset().filter(ano_de_fabricacao__icontains=ano)


    def lista_veiculos_por_modelo(self, modelo):
        return self.get_queryset().filter(modelo__icontains=modelo)


class Veiculo(models.Model):
    tipo = models.CharField('Tipo', max_length=100)
    ano_de_fabricacao = models.IntegerField('Ano de Fabricação')
    modelo = models.CharField('Modelo', max_length=100)
    cor = models.CharField('Cor', max_length=100)

    class Meta:
        db_table = 'veiculo'

    objects = GerenciadorVeiculo()

class GerenciadorGaragem(models.Manager):

    def lista_veiculos(self, id):
        garagem = self.get_queryset.filter(id__exact=id)
        return garagem.veiculos.all()

class Garagem(models.Model):
    nome = models.CharField('Garagem', max_length=100, default='None')
    consumidor = models.ForeignKey(Pessoa, on_delete=models.PROTECT, editable=False)
    veiculos = models.ManyToManyField(Veiculo)

    class Meta:
        db_table = 'garagem'

    objects = GerenciadorGaragem




