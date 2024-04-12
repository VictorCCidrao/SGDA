from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import CriarUsuarioForm, LoginForm
from .models import Aluno
import openpyxl
import pandas as pd
import os


# VIEWS
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
            matricula = form.cleaned_data["matricula"]
            arquivo_excel = "media/matriculas.xlsx"

            if validar_matricula(matricula, arquivo_excel):
                user = form.save()
                nome = obter_nomes(matricula, arquivo_excel)
                Aluno.objects.create(user=user, matricula=matricula, nome_completo=nome)
                return redirect("sucesso")
            else:
                # Matrícula inválida
                if os.path.exists(arquivo_excel):
                    print("O arquivo no diretório existe:", True)
                else:
                    print("O arquivo no diretório NÃO existe", False)

                messages.error(
                    req, "Matrícula inválida. Por favor, verifique sua matrícula."
                )
                return redirect("register")
        else:
            messages.error(req, "Erro no formulário. Por favor, verifique os campos.")
            # Redirecionar de volta para o formulário de registro
            return redirect("register")
    else:
        form = CriarUsuarioForm()
    return render(req, "register.html", {"form": form})


def sucessView(req):
    return render(req, "register_success.html")


# METODOS ABAIXO ----------------------------------------------------------------------------------------------


# Validação de matricula usando o PANDAS
def validar_matricula(matricula, arquivo_excel):
    try:
        df = pd.read_excel(arquivo_excel)
        # Verificar se a matrícula está presente na coluna 'Matrícula' do DataFrame
        matricula_is_registed = str(matricula) in df["Matricula"].astype(str).values
        print("Matrícula está registrada?: ", matricula_is_registed)
        print("Valores na coluna Matrícula:", df["Matricula"].unique())

        return matricula_is_registed
    except Exception as e:
        # Trate exceções de leitura de arquivo aqui
        print(e)
        return False


def obter_nomes(matricula, arquivo_excel):
    try:
        df = pd.read_excel(arquivo_excel)
        if str(matricula) in df["Matricula"].astype(str).values:
            # Encontra o nome correspondente à matrícula
            nome = df.loc[df["Matricula"].astype(str) == str(matricula), "Nome"].iloc[0]
            return nome
        else:
            return None
    except Exception as e:
        # Trate exceções de leitura de arquivo aqui
        print(e)
        return False
