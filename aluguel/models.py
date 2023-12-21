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