from django.contrib import admin
from django.urls import path,include
from .views import Roles_View,SignUp
urlpatterns = [
    
    path('roles/', Roles_View.as_view()),
    path('signup/',SignUp.as_view()),
    
]