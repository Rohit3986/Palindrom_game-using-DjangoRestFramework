from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

class Game(models.Model):
    player=models.OneToOneField(to=User,on_delete=models.CASCADE,primary_key=True)
    string=models.CharField(max_length=6,default="",blank=True)
    created_on=models.DateTimeField(auto_now_add=True)

