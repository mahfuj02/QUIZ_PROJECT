from django.contrib import admin
from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('userupdate/<int:user_id>/',views.update,name = 'userupdate'),
    path('user/<int:user_id>/',views.User_profiel,name = 'userprofile'),
    path('logout/',views.logout_view,name = 'logout'),
    path('login/',views.login_view, name = 'login'),
    path('signup/',views.signup_view, name = 'signup'),
    path('dailyscore/',views.Daily_View, name = 'dailyscore'),
    path('weeklyscore/',views.Weekly_View, name = 'weeklyscore'),
    path('allscore/',views.All_View, name = 'allscore'),



]
