from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Carro(models.Model):

  CAMBIO = [
        ("Manual", "Manual"),
        ("Automático", "Automático"),
  ]
  TIPOS = [
        ("Gasolina", "Gasolina"),
        ("Diesel", "Diesel"),
        ("Flex", "Flex"),
        ("Elétrico", "Elétrico"),
  ]
  STATUS = [
        ("Disponivel", "Disponivel"),
        ("Alugado", "Alugado"),
  ]

  marca = models.CharField(max_length=200)
  modelo = models.CharField(max_length=200)
  ano_fabricacao = models.PositiveSmallIntegerField("Ano de Fabricação")
  quant_passageiros = models.PositiveSmallIntegerField("Quantidade de Passageiros")
  transmissao = models.CharField("Transmissão", max_length=200, choices=CAMBIO, default="Manual")
  combustivel = models.CharField("Combustivel", max_length=200, choices=TIPOS, default="Hibrido")
  disponibilidade = models.CharField("Disponibilidade", max_length=200, choices=STATUS, default="Disponivel")
  preco = models.PositiveIntegerField("Preço do aluguel por dia")
  foto = models.ImageField(upload_to='avatares', blank=True, null=True)

  def __str__(self):
    return self.modelo
  
  class Meta:
    verbose_name = "Carro"
    verbose_name_plural = "Carros"

class Cliente(models.Model):
    
    nome = models.CharField("Nome", max_length=200)
    data_nascimento = models.DateField("Data de Nascimento", null=True, blank=True)
    email = models.EmailField("Email")
    idade = models.PositiveSmallIntegerField("Idade", null=True, blank=True)
    avatar = models.ImageField("Foto", upload_to='avatares', blank=True, null=True)
    user = models.OneToOneField(get_user_model(), verbose_name="Usuário",on_delete=models.CASCADE, related_name="cliente")

    def __str__(self):
        return self.nome + " " + self.email
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Aluguel(models.Model):
    
    carro = models.OneToOneField(Carro, verbose_name="Carro",on_delete=models.CASCADE, related_name="carro")
    cliente = models.OneToOneField(Cliente, verbose_name="Usuário",on_delete=models.CASCADE, related_name="cliente")
    data_inicial = models.DateField("Data Inicial")
    data_final = models.DateField("Data Final", blank=True, null=True)
    
    def __str__(self):
        return self.cliente + " - " + self.carro
    
    class Meta:
        verbose_name = "Aluguel"
        verbose_name_plural = "Aluguéis"

