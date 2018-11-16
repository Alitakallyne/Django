from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import User, Categoria
from .forms import LoginForm,CategoriaForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class RegisterView(CreateView):

	model = User
	template_name = 'anuncio/register.html'
	form_class = LoginForm
	success_url = reverse_lazy('anuncio:login')



def index(request):
	return render(request,'anuncio/index.html');

def sobre(request):
	return render(request,'anuncio/sobre.html');
	
class CategoriaView(SuccessMessageMixin, CreateView):
	model = Categoria
	template_name = 'categoria/add_categoria.html'
	success_message = "Categoria criada com sucesso!"
	form_class = CategoriaForm
	success_url = reverse_lazy('anuncio:index')