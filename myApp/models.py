from django.db import models
from datetime import timedelta 
from django.utils.timezone import now
# Create your models here.

class Book(models.Model):
    bk_name = models.CharField(max_length=100)
    bk_number= models.IntegerField() 


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)


def one_week_hence():
    return now() + timedelta(weeks=1)