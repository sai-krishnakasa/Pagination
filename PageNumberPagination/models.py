from django.db import models

class student(models.Model):
    name=models.CharField(max_length=100)
    roll_no=models.CharField(max_length=100)
