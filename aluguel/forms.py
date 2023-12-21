from django.forms import ModelForm, EmailField, CharField
from .models import Carro, Cliente, Aluguel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):

    first_name = CharField(max_length=150, label="Nome")
    last_name = CharField(max_length=150, label="Sobrenome")
    email = EmailField(max_length=200, label="Email")
    
    class Meta:
        model = get_user_model()
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2' ]

class CarroForm(ModelForm):

  class Meta:
    model = Carro
    fields = '__all__'

class ClienteForm(ModelForm):
    # def clean_idade(self):
    #     idade = self.cleaned_data["idade"]

    #     if idade is not None and idade < 18:
    #        raise  ValidationError("O autor não pode ter menos de 18 anos.", code='menor_idade')
        
    #     return idade
    class Meta:
        model=Cliente
        fields='__all__'

class AluguelForm(ModelForm):

  class Meta:
    model = Aluguel
    fields = '__all__'