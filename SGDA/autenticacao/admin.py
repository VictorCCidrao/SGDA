from django.contrib import admin
from .models import Aluno, Nutricionista

# Register your models here.

# PRECISO REGISTRAR AS CLASSES PARA QUE APAREÇAM NO /ADMIN
admin.site.register(Aluno)
admin.site.register(Nutricionista)
