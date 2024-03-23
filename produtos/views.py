from django.contrib import messages
from django.shortcuts import (render, redirect, get_list_or_404)
from produtos.models import Produtos
from produtos.forms import ProdutosForm

def registar_produto(request):
    form = ProdutosForm()
    if request.method == "POST":
        form = ProdutosForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.registrado_por = request.user
            produto.save()
            messages.success(request, "Produto cadastrado com sucesso!")
            return redirect("index")
        
    context = {"nome_pagina": "Registrar produto", "form": form}
    return render(request, "registrar_produto.html", context)

def informacoes_produto(request, id):
    produto = get_list_or_404(Produtos, id=id)
    context = {"nome_pagina": "Informações do produto", "produto": produto}
    return render(request, "informacoes_produto.html", context)