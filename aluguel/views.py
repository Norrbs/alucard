from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import RegistrationForm, CarroForm
from .models import Carro


# Create your views here.
class HomeView(TemplateView):
  template_name = 'home.html'

  def __str__(self):
    return self.modelo
  
class ListarCarroView(ListView):
   model=Carro
   template_name='carro/listar.html'
   context_object_name='carros'
   paginate_by='6'

class DetalharCarroView(DetailView):
   model=Carro
   template_name='carro/detalhar.html'
   context_object_name='carro'

class CadastrarCarroView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Carro
    template_name = "carro/cadastrar.html"
    form_class = CarroForm
    permission_required='aluguel.add_carro'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Carro cadastrado com sucesso!")
        return reverse('listar-carro')
   
class AtualizarCarroView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Carro
    template_name = "carro/atualizar.html"
    form_class = CarroForm
    permission_required='aluguel.change_carro'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Carro atualizado com sucesso!")
        return reverse('listar-carro')
    
class DeletarCarroView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Carro
    template_name = "carro/carro_confirm_delete.html"
    permission_required='aluguel.delete_carro'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Carro deletado com sucesso!")
        return reverse('listar-carro')
    
class RegistrationView(CreateView):
    template_name = "registration/registration.html"
    model = get_user_model()
    form_class = RegistrationForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Cadastro realizado com sucesso!")
        return reverse('home')
