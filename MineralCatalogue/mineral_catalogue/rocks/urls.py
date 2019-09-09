from . import views
from django.urls import path

app_name = "rocks"

urlpatterns = [

    path('home/<str:letter>/', views.index, name="index"),
    path('home/<int:pk>/', views.details, name="details"),
    path('home/random', views.random, name="random"),


]