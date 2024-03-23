from django.contrib import messages
from django.shortcuts import render, redirect
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