from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=250)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
class Quarto(models.Model):
    apartamento = models.PositiveIntegerField()
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return str(self.apartamento)
    
class Consumo(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    hospedagem = models.ForeignKey('Hospedagem',on_delete=models.CASCADE)

class Hospedagem(models.Model):
    data_entrada = models.DateField()
    data_saida = models.DateField()
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    cliente = models.ForeignKey('Cliente',on_delete=models.CASCADE)
    quarto = models.ForeignKey('Quarto',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cliente.nome + " - " + self.quarto.numero