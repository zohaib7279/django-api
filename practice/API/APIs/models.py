# APIs/models.py
from email.headerregistry import Address
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    Address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
