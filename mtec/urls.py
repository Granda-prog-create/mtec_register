from django.contrib import admin
from django.urls import path
from users.views import index
from produtos.views import (registar_produto, informacoes_produto, finalizar_venda)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("registrar-produto/", registar_produto, name="registrar_produto"),  
    path("produtos/<int:id>/", informacoes_produto, name="informacoes_produto"),
    path("vendas/<int:id>/finalizar-venda", finalizar_venda, name="finalizar_venda"),

]