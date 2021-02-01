from django.db import models
from django.contrib import auth
from .forms import UserRegistrationForm
from django.contrib.auth.models import User,PermissionsMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate
#Create your models here.
#User = get_user_model()

class UserLeaderboard(models.Model):
    idname = models.OneToOneField(User, default="", on_delete = models.CASCADE)
    dailyscore = models.IntegerField(default=0)
    weeklyscore = models.IntegerField(default=0)
    allscore = models.IntegerField(default=0)
 