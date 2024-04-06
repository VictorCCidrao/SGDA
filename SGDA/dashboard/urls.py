from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexDash, name='dashboard'),
    path('relatorio', views.relatorio, name='relatorio'),
    path('settings', views.settings, name='settings'),
    path('help', views.help, name='help')
]
