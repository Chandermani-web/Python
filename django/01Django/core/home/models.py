from django.db import models

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    age = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.username} ({self.email}), Age: {self.age}"