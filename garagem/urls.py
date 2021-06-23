from django.urls import path, include
from . import views

app_name = 'gerencia_garagens.garagem'

urlpatterns = [

    path('cadastrarveiculo/', views.cadastrarveiculo, name='cadastrarveiculo'),
    path('cadastrar', views.cadastrar, name='cadastrar')
    #path('garagem/adicionaveiculo', views.adicionarveiculo, name='adicionarveiculo')
    #path('garagem/listaveiculos', views.listarveiculos, name='listarveiculos')

]
