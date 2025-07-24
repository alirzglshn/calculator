from django.db import models

# Create your models here.

class Calc(models.Model):
    first_number = models.IntegerField()
    second_number = models.IntegerField()
    operation = models.CharField(max_length=8)
