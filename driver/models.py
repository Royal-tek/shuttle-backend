from django.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    othernames = models.CharField(max_length=256)
    platenumber = models.CharField(max_length=15)
    

