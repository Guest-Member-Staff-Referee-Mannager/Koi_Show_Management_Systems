from django.db import models
from django import forms

# Create your models here.
class competition (models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    # active = models.BooleanField()
    def __str__(self):
        return f"{self.name} {self.start_date}"
    
class register (models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=12)
    birthDay = models.DateField()
    competitions = models.ManyToManyField(competition)
    start_date = models.DateField()
    gender = models.CharField(max_length=10)  
    age = models.IntegerField()  
    size = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.name} - {self.start_date}"