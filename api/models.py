from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)

# Create your models here.
class Candidate(models.Model):
    candidate_name=models.CharField(max_length=100)
    party=models.CharField(max_length=50)
    def __str__(self):
        return self.candidate_name
    

class Student(models.Model):
    name=models.CharField(max_length=100)
    mark=models.IntegerField()
    def __str__(self):
        return self.name

