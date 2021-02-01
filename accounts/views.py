from django.shortcuts import render, redirect
from accounts.forms import UserRegistrationForm, UserLoginForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, authenticate, login , logout
from django.contrib.auth.models import User
from .models import UserLeaderboard
User = get_user_model()

def User_profiel(request,user_id):
    user = User.objects.get(pk=user_id)
    diction = {"user":user}
    template_name = 'accounts/user.html'
    return render(request, template_name, context= diction)

def signup_view(request, *args, **kwargs):
    
    form = UserRegistrationForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()

           # Leaderboard = form.objects.create(username = form.username , daily_point = 0)
            return redirect('pages:index')

    
    template_name = 'accounts/index.html'

    diction = {'form':form}
    return render(request, template_name , context=diction)

def login_view( request ):
    next = request.GET.get('next')
    template_name = 'accounts/login.html'
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username= username , password =password)
            login(request, user)
            if next:
                return redirect(next)
            return redirect('pages:index')
    diction = {'form':form,'check':"Cheking Ok!"}
    return render(request, template_name , context=diction )

def logout_view(request):
    logout(request)
    return redirect('pages:index')

def update(request,user_id):
    user_update = User.objects.get(pk=user_id)
    form = UserRegistrationForm(instance=user_update)
    if request.method =="POST":
        form = UserRegistrationForm(request.POST, instance=user_update)
        if form.is_valid():
            form.save(commit=True)
            return redirect('accounts:userprofilepy')
    
    diction = {"form":form}
    return render(request, "accounts/userupdate.html", context=diction)


def Daily_View(request):
   
    data = UserLeaderboard.objects.all().order_by('-dailyscore')
    diction = {"score":data}
    template_name = 'quiz/dailyscore.html'
    return render(request, template_name , context=diction)
def Weekly_View(request):
   
    data = UserLeaderboard.objects.all().order_by('-weeklyscore')
    diction = {"score":data}
    template_name = 'quiz/weeklyscore.html'
    return render(request, template_name , context=diction)
def All_View(request):
   
    data = UserLeaderboard.objects.all().order_by('-allscore')
    diction = {"score":data}
    template_name = 'quiz/allscore.html'
    return render(request, template_name , context=diction)