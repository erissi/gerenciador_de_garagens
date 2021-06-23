from django.db import models


# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=11)
    email = models.CharField('Email', max_length=100, unique=True)

    class Meta:
        db_table = 'pessoa'




#class Administrador(Pessoa):


#    class Meta:
#        db_table = 'administrador'

#class Consumidor(Pessoa):

#    class Meta:
#        db_table = 'consumidor'
