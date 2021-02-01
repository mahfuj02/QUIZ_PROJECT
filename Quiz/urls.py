from django.contrib import admin
from django.urls import path
from . import views
from accounts.views import login_view
app_name = 'quiz'
urlpatterns = [

    path('login/', login_view, name='login'),
    path('quiz_one/', views.Quiestion_view1, name='onemin'),
    path('quiz_three/', views.Quiestion_view2, name='threemin'),
    path('longquiz_five/', views.Quiestion_view, name='fivemin'),

]
