from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("<str:name>", views.greet, name="greet"),
    path("gayheart", views.gayheart, name="gayheart"),
    path("jessie", views.jessie, name="jessie")
]