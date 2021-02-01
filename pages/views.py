from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    diction = {'title':"Home Page"}
    return render(request, 'pages/index.html', context = diction)

