from django.db import models
from random import choice




    
class Cliente_sms(models.Model):
    def __unicode__(self):
        return self.nome
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=75)
    celular = models.CharField(max_length=15)
    
   

