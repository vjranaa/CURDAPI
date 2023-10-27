from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    password = models.CharField(max_length=30)
class Meta:
    db_table = "student"