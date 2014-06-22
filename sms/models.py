from django.db import models

class Frase(models.Model):
    
    frase_dia = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=200)
    def __unicode__(self):
        return self.frase_dia

    


