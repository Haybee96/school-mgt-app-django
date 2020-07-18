from django.db import models
from datetime import datetime


class Student(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=12, unique=True)
    level = models.CharField(max_length=20, default='no level')
    created = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.firstname + ' ' + self.lastname
