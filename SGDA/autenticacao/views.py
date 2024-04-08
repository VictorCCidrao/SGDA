from django.shortcuts import render


# Create your views here.
def loginView(req):
    return render(req, "login.html")


def registerView(req):
    return render(req, "register.html")
