from django.urls import path, include
from . import views

app_name = 'gerencia_garagens.pessoa'

urlpatterns = [

    #path('cadastrarusuario/', views.cadastrarusuario, name='cadastrarusuario'),
    path('cadastrarpessoa/', views.cadastrarusuario, name="cadastrarusuario"),
]
