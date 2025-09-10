from django.db import models
from datetime import datetime

# Create your models here.

class Imagem(models.Model):
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),

    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.CharField(max_length=50, choices=OPCOES_CATEGORIA, default="")
    descricao = models.TextField(max_length=150, null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True, null=False)
    publicada = models.BooleanField(default=True)
    data_imagem = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome
