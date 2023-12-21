from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.ListarCarroView.as_view(), name='listar-carro'),
    path('cadastrar', views.CadastrarCarroView.as_view(), name='cadastrar-carro'),
    path('<int:pk>', views.DetalharCarroView.as_view(), name='detalhar-carro'),
    path('atualizar/<int:pk>', views.AtualizarCarroView.as_view(), name='atualizar-carro'),
    path('deletar/<int:pk>', views.DeletarCarroView.as_view(), name='deletar-carro'),

]