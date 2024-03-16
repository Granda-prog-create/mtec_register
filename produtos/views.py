from django.shortcuts import render
from produtos.forms import ProdutosForm

def registar_produto(request):
    form = ProdutosForm()
    context = {"nome_pagina": "Registrar produto", "form": form}
    return render (request, "registrar_produto.html", context)
