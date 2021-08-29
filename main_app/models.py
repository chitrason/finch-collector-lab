from django.db import models

# Create your models here.

class Finch(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField() 

#this is what lets the name show in the admin portal vs object numbers
  def __str__(self):
    return self.name  