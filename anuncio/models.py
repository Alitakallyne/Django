import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, UserManager, PermissionsMixin)
from django.core import validators
import re

"""
class CadastroUsuario(models.Model):

	name = models.CharField(verbose_name=('Nome Completo'),max_length=100)
	contato = models.CharField(verbose_name=('Contato'),max_length=100)
	endereco = models.TextField(verbose_name=('Endereço'),max_length=100)
	email = models.EmailField(verbose_name=('Email'),max_length=100)
	username = models.CharField(verbose_name=('Nome de Usuário'),max_length=40)
	password = models.CharField(verbose_name=('Senha'),max_length=50)
"""

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'E-mail / Usuário', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
            )
        ], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    
    """ Método deletar a imagem (avatar) quando alterada ou excluida """
    def delete(self):
        self.avatar.delete()
        return super(Dentist, self).delete()


    def _str_(self):
        return self.first_name or self.username

    def get_full_name(self):
        return ('%s  %s') % (self.first_name, self.last_name)

    def get_short_name(self):
        return str(self).split(" ")[0]

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class Categoria(models.Model):
    titulo = models.CharField(verbose_name="Título Categoria", max_length=200)

    def __str__(self):
        return self.titulo

        

class Anuncio(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=200)
    descricao = models.TextField(verbose_name="Descrição")
    preco = models.DecimalField(verbose_name="Preço", max_digits=5, decimal_places =2)
    tempo_uso = models.DateField(verbose_name="Data de compra")
    data_cadastro = models.DateTimeField(verbose_name="Data de criação", default=timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagem = models.ImageField(verbose_name="Imagem",)

    def __str__(self):
        return self.titulo
        
	
class Question(models.Model):
	question_text = models.CharField(verbose_name="Texto da questão", max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text
		
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text
