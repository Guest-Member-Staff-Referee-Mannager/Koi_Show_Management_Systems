from django.contrib import admin
from django.urls import include, path
from .import views
urlpatterns = [
    path('', views.home, name= "index"),
    path('competitions', views.competitions, name= "competitions"),
    path('competition-edit', views.competition_edit, name= "competition-edit"),
]

