from django.urls import path
from . import views

urlpatterns =[
    path('home',views.home,name='index'),
    path('login',views.loginpage,name='login'),
    path('',views.signup,name='signup')
]