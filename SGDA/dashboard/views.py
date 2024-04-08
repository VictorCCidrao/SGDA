from django.shortcuts import render


# Create your views here.


def indexDashboardView(req):
    # VAI DEPENDER DO TIPO DE USUÁRIO (PESQUISAR SOBRE ISSO DEPOIS)
    # Uma view que determina o tipo de usuário logado e renderiza o template apropriado com base no papel do usuário.
    # Esta view pode consultar o modelo UserProfile para determinar o papel do usuário.
    return render(req, "base/dashboard_base.html")


# def relatorioView(req):
#     return render(req, "relatorio.html")


def settingsView(req):
    return render(req, "settings.html")


def helpView(req):
    return render(req, "help.html")
