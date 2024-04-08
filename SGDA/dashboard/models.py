from django.db import models
from django.contrib.auth.models import User
from autenticacao.models import Aluno, Admin

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    # Outros campos comuns para UserProfile

    # Relacionamento polimórfico com Aluno e Admin
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE, null=True, blank=True)
    admin = models.OneToOneField(Admin, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username  # Retorna o nome de usuário do UserProfile
