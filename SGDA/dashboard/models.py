from django.db import models
from django.contrib.auth.models import User
from autenticacao.models import Aluno, Nutricionista

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    img = models.ImageField(upload_to="profile_pics", blank=True, null=True)

    def is_aluno(self):
        return Aluno.objects.filter(user=self.user).exists()

    def is_admin(self):
        return Nutricionista.objects.filter(user=self.user).exists()

    def __str__(self):
        return self.user.username  # Retorna o nome de usuário do UserProfile
