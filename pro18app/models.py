from django.db import models


# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media')

def __str__(self):
    return self.name
