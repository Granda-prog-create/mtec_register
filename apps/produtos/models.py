import re
from django.db import models
from django.conf import settings

class Produtos(models.Model):
    STATUS_PRODUTO = [
        ("AGUARDANDO", "Aguardando a venda"),
        ("NO_ESTOQUE", "No estoque"),
        ("FINALIZADA", "Venda finalizada")
    ]

    status = models.CharField(verbose_name="Status", max_length=10, choices=STATUS_PRODUTO, default="AGUARDANDO")

    nome_produto = models.CharField(verbose_name="Produto", max_length=200)

    valor_produto = models.CharField(verbose_name="Valor", max_length=200)

    data_venda = models.DateField(verbose_name="Data da venda", auto_now=False, auto_now_add=False)

    quantidade_venda = models.PositiveSmallIntegerField(verbose_name="Quantidade de produtos")

    vendedor_responsavel = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Vendedor Responsável", on_delete=models.SET_NULL, blank=True, null=True)

    horario_venda = models.DateTimeField(verbose_name="Horário da venda", auto_now_add=True, blank=True, null=True)

    supervisor = models.CharField(verbose_name="Supervisor", max_length=194, blank=True) 
 
    def get_horario_venda(self):
        if self.horario_venda:
            return self.horario_venda
        return "O horário da venda não foi registrado"
    
    def get_vendedor_responsavel(self):
        if self.vendedor_responsavel:
            return self.vendedor_responsavel
        return "Produto aguardando autorização..."
    
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        db_table = "produtos"

    def __str__(self):
        return self.nome_produto
