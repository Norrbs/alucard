from django.db import models

# Create your models here.
class Carro(models.Model):

  CAMBIO = [
        ("Manual", "Manual"),
        ("Automático", "Automático"),
  ]
  TIPOS = [
        ("Gasolina", "Gasolina"),
        ("Diesel", "Diesel"),
        ("Hibrido", "Híbrido"),
        ("Eletrico", "Elétrico"),
  ]
  STATUS = [
        ("Disponivel", "Disponivel"),
        ("Alugado", "Alugado"),
  ]

  marca = models.CharField(max_length=200)
  modelo = models.CharField(max_length=200)
  ano_fabricacao = models.PositiveSmallIntegerField()
  quant_passageiros = models.PositiveSmallIntegerField()
  transmissao = models.CharField("Câmbio", max_length=100, choices=CAMBIO, default="Manual")
  combustivel = models.CharField("Combustivel", max_length=100, choices=TIPOS, default="Hibrido")
  disponibilidade = models.CharField("Disponibilidade", max_length=100, choices=STATUS, DEFAULT="Disponivel")
  preco = models.PositiveIntegerField()