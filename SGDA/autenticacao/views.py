from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CriarUsuarioForm, LoginForm


# Create your views here.
def loginView(req):
    form = LoginForm()
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user)
                # Redirecione para a página inicial ou para onde desejar
                return redirect("dashboard")
            else:
                form = LoginForm()
    return render(req, "login.html", {"form": form})


def registerView(req):
    if req.method == "POST":
        form = CriarUsuarioForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("sucesso")
    else:
        form = CriarUsuarioForm()
    return render(req, "register.html", {"form": form})


def sucessView(req):
    return render(req, "register_success.html")
