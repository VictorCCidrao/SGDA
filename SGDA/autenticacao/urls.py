from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginView, name="dashboard"),
    path("register/", views.registerView, name="dashboard"),
]
