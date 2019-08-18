from django.db import models

# Create your models here.

class UserData(models.Model):
	username =  models.TextField()
	password = models.TextField()
