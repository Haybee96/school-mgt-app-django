from django.db import models
from students.models import Student
from datetime import datetime

class Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    unit = models.IntegerField()
    created = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.title + ' ' + self.code

