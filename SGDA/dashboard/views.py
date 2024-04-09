from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import UserProfile
from autenticacao.models import Aluno, Nutricionista
from autenticacao.views import loginView
from django.urls import reverse

# Create your views here.
def indexDashboardView(request):
     # Verifica se o usuário está autenticado
    if request.user.is_authenticated:
        # Verifica se o usuário logado está na tabela autenticacao.Aluno
        if Aluno.objects.filter(user=request.user).exists():
            return render(request, "dashboard_aluno.html")
        # Verifica se o usuário logado está na tabela autenticacao.Nutricionista
        elif Nutricionista.objects.filter(user=request.user).exists():
            return render(request, "dashboard_admin.html")
        # else:
        #     # Caso não esteja em nenhum grupo específico, redireciona para a página inicial
        #     return redirect(reverse('dashboard:index'))
    else:
        # Caso não esteja autenticado, redireciona para a rota de login da aplicação autenticacao
        return redirect(reverse('login'))

def settingsView(req):
    return render(req, "settings.html")


def helpView(req):
    return render(req, "help.html")
