from django.contrib import admin
from .models import Aluno

# PRECISO REGISTRAR AS CLASSES PARA QUE APAREÇAM NO /ADMIN
admin.site.register(Aluno)