from django.urls import path
from . import views

urlpatterns = [
    # Esta rota (dashboard) pode ser protegida por autenticação para garantir que apenas usuários logados possam acessar o dashboard.
    path("", views.indexDashboardView, name="dashboard"),
    # path("relatorio", views.relatorioView, name="relatorio"),
    path("settings", views.settingsView, name="settings"),
    path("help", views.helpView, name="help"),
]
