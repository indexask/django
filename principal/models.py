from django.db import models

class Estado(models.Model):
    id= models.AutoField(primary_key=True)
    estado= models.CharField(max_length=25)
    def __str__(self):
        return str(self.id)+" "+self.estado
