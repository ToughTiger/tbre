from datetime import datetime
from django.db import models

# Realtor Model

class Realtor(models.Model):
    name= models.CharField(max_length=200)
    photo= models.ImageField(upload_to= 'photos//%Y/%m/%d/')
    description= models.TextField(blank=True)
    phone = models.CharField(max_length= 20)
    email= models.CharField(max_length=100)
    is_mvp=models.BooleanField(default=False)
    join_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

