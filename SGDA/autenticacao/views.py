from django.shortcuts import render, redirect
from .forms import CriarUsuarioForm

# Create your views here.
def loginView(req):
    return render(req, "login.html")

def registerView(req):
    if req.method == 'POST':
        form = CriarUsuarioForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect ('sucesso')
    else:
        form = CriarUsuarioForm()
    return render(req, 'register.html', {'form': form})

def sucessView(req):
    return render(req, "register_success.html")