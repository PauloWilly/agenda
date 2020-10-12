from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model): #classe que representa uma tabela
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True) #criando um registro, ele exibe a hora atual
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'evento' #exijo que a tabela chame "evento" e não "core_evento" posto pelo Django automaticamente

    def __str__(self):
        return self.titulo

