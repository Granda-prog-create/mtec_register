from django.db import models

class Cliente(models.Model):
    user = models.OneToOneField("users.User", verbose_name="Usuário", on_delete=models.PROTECT)
    nome_completo = models.CharField(verbose_name="Nome completo", max_length=194)
    cpf = models.CharField(verbose_name="CPF", max_length=11)
    telefone = models.CharField(verbose_name="Telefone", max_length=15) 
    data_nascimento = models.DateField(verbose_name="Data de nascimento", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = "cliente"

    def __str__(self):
        return self.nome_completo  