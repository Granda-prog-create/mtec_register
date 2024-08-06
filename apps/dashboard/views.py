from django.shortcuts import render
from produtos.models import Produtos

def index(request):
    todos_produtos = Produtos.objects.all()

    produtos_estoque = todos_produtos.filter(status="Em estoque")

    produtos_recebidos = todos_produtos.filter(status="Recebidos") 

    produtos_vendidos = todos_produtos.filter(status="Vendas finalizadas") 

    venda_total = todos_produtos.filter(status="Vendas totais")

    context = {"nome_pagina": "Seu estoque", 
               "todos_produtos": todos_produtos, 
               "produtos_estoque": produtos_estoque.count(), 
               "produtos_recebidos": produtos_recebidos.count(),
               "produtos_vendidos": produtos_vendidos.count(),
               "venda_total": venda_total.count(),
               }

    return render(request, "index.html", context)