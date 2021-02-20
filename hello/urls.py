from django.urls import path

from . import views

urlpatterns = [
  path("<str:name>", views.greet, name="greet"),
  path("", views.index, name="index"),
  path("dody", views.dody, name="dody"),
  path("retal", views.retal, name="retal")
  
]