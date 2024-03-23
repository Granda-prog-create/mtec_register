from django.db import models

class Produtos(models.Model):
    nome_produto = models.CharField(verbose_name="Produto", max_length=200)
    valor_produto = models.CharField(verbose_name="Valor", max_length=200)
    data_venda = models.DateField(verbose_name="Data da venda", auto_now=False, auto_now_add=False)
    quantidade_venda = models.PositiveSmallIntegerField(verbose_name="Quantidade de produtos")
    vendedor = models.CharField(verbose_name="Vendedor", max_length=194, blank=True, null=True)
    horario_venda = models.DateTimeField(verbose_name="Horário da venda", auto_now_add=True, blank=True, null=True)
    supervisor = models.CharField(verbose_name="Supervisor", max_length=194, blank=True)
    # registrado_por = models.ForeignKey("self", verbose_name="Responsável pelo registro", on_delete=models.PROTECT, blank=True, null=True) Opcional!

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        db_table = "produtos"

    def __str__(self):
        return self.nome_produto