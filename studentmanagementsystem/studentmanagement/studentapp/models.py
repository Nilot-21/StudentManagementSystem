from django.db import models
class Student(models.Model):
    roll_number=models.PositiveIntegerField()
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    field_of_study=models.CharField(max_length=100)
    gpa=models.FloatField()

    def __str__(self):
        return f'Student:{self.first_name} {self.last_name}'
# Create your models here.
