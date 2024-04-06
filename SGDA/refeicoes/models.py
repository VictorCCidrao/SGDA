from email.message import EmailMessage
from django.db import models
from django.contrib.auth.models import User


# #TABELA IMPORTADA USER TEM COMO ATRIBUTOS PADRÕES: 
#     USERNAME
#     EMAIL
#     SENHA 
#     NOME 
#     SOBRENOME  

# CLASSE ALUNO HERDA A TABELA USER, E SÓ ACRESCENTA OS ATRIBUTOS USER E MATRICULA.

# O IMPORT USER PODE DEFINIR USUARIOS ADMINS QUE PODE ENTRAR NA ROTA /ADMIN   "python .\manage.py createsuperuser"

# "python .\manage.py makemigrations" PARA FAZER ANALISE E PREPARAÇÃO DOS MODELOS EM SQL E O "python .\manage.py migrations" É QUEM UPA ELES LÁ.

class Aluno(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)  #ForeingKey é a chave estrangeira da tabela USER, ou seja, pelo atributo "user" consigo acessar todos os outros da tabela User. ex: user.email
    matricula = models.CharField(max_length=100, unique=True)
    