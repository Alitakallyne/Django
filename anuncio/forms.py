from django import forms
#from django.contrib.auth.models import User
from . models import User,Categoria
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm

class LoginForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

"""class LoginForm(forms.Form):
	class Meta:
		model = CadastroUsuario
		fields = ('nome','contato','endereco','email','username','password')
		def __init__(self,*args,**kwargs):
			super().__init__(*args,**kwargs)
			self.helper = FormHelper()
			self.helper.form_method = 'post'
			self.helper.add_input(Submit('submit','Save Cadastro'))"""

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'is_staff']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'is_active', 'is_staff']

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['titulo']
        