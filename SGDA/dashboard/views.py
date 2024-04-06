from django.shortcuts import render

# Create your views here.
def indexDash(req):
    return render(req, 'index.html')

def relatorio(req):
    return render(req, 'relatorio.html')

def settings(req):
    return render(req, 'settings.html')

def help(req):
    return render(req, 'help.html')