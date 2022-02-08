from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.

class Evento(models.Model): #classe que representa uma tabela
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True) #permitindo os campos serem preenchidos ou não, através de "(blank=True, null=True)"
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True) #criando um registro, ele exibe a hora atual
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #cascade = se o usuário for escluído da aplicação, tb serão excluídos todos os eventos dele

    class Meta:
        db_table = 'evento' #exijo que a tabela chame "evento" e não "core_evento" posto pelo Django automaticamente

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y às %H:%M hrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')# formatando no padrão que o navegador entende

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False