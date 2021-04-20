from django.db import models
from datetime import datetime
from realtors.models import Realtor
# Listing Model...


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length= 120)
    address = models.CharField(max_length= 120)
    city= models.CharField(max_length= 120)
    state = models.CharField(max_length = 20, blank= True)
    pincode = models.CharField(max_length= 20)
    descripting = models.TextField(max_length= 120)
    price = models.IntegerField(default=0)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    parking = models.IntegerField(default=0)
    builtupArea = models.IntegerField()
    carpetArea = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    



