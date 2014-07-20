from django.db import models
from random import choice



class Frase(models.Model):
    def __unicode__(self):
        return self.frase_dia
    frase_dia = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=200)
    
    def quote(self):
        return choice(frase_dia)
    
class Cliente_sms(models.Model):
    def __unicode__(self):
        return self.nome
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=75)
    celular = models.CharField(max_length=15)
    
   

