from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginView, name="login"),
    path("register/", views.registerView, name="register"),
    path("success/", views.sucessView, name="sucesso"),
]
