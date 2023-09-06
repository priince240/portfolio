from django.db import models
from datetime import datetime
# Create your models here.
class visitermodel(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=11)
    query=models.CharField(max_length=1000)
    date=models.DateTimeField(datetime.now().strftime("%A,%d,%Y"))
    
    
    def __str__(self):
        return self.name