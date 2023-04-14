from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registerPage, name='register'),
    path("login/", views.loginPage, name='login'),
    path("home/", views.homePage, name='home'),
    path("prediction/", views.prediction, name='prediction'),
    path("results/", views.result, name='results'),
    path("intro/", views.intro, name='intro'),
    path("houseprices/", views.housePrice, name='houseprices'),
    path("logout/", views.logoutUser, name='logout'),
]
