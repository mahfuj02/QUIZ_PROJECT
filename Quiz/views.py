from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required
from accounts import views

def Quiestion_view(request,*views):
    if not request.user.is_authenticated:
        return render(request,'accounts/login.html')
    questions = models.Quiz.objects.all()
    diction = {"questions":questions}
    template_name = 'quiz/index.html'
    return render(request, template_name , context=diction)

def Quiestion_view1(request,*views):
    if not request.user.is_authenticated:
        return render(request,'accounts/login.html')
    questions = models.Quiz.objects.all()
    diction = {"questions":questions}
    template_name = 'quiz/oneminquiz.html'
    return render(request, template_name , context=diction)

def Quiestion_view2(request,*views):
    if not request.user.is_authenticated:
        return render(request,'accounts/login.html')
    questions = models.Quiz.objects.all()
    diction = {"questions":questions}
    template_name = 'quiz/threeminquiz.html'
    return render(request, template_name , context=diction)

# Create your views here.
