from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from produtos.models import Produtos
from produtos.forms import ProdutosForm, AutorizaVendaForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
def informacoes_produto(request, id):
    produto = get_object_or_404(Produtos, id=id)
    form = AutorizaVendaForm()
    if request.method == "POST":
        form = AutorizaVendaForm(request.POST, instance=produto)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.status = "NO_ESTOQUE" 
            produto.horario_autorizacao = timezone.now()
            produto.save()
            messages.success(request, "Venda realizada com sucesso!")
            return redirect("index")

    vendedor_responsavel = produto.vendedor_responsavel  
    context = {"nome_pagina": "Informações do produto", "produto": produto, "vendedor_responsavel": vendedor_responsavel, "form": form}  
    return render(request, "informacoes_produto.html", context)

@login_required
def finalizar_venda(request, id):
    produto = get_object_or_404(Produtos, id=id)
    if request.method == "POST":
        produto.status = "FINALIZADO"
        produto.horario_saida = timezone.now()
        produto.save()
        messages.success(request, "Venda finalizada com sucesso!")
        return redirect("index")

    else:
        return HttpResponseNotAllowed(["POST"], "Método não permitido")

@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produtos, id=id)
    form = ProdutosForm(instance=produto)
    
    if request.method == "POST":
        form = ProdutosForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto atualizado com sucesso!")
            return redirect("index")
    
    context = {"nome_pagina": "Editar produto", "form": form, "produto": produto}
    return render(request, "editar_produto.html", context)

@login_required
def excluir_produto(request, id):
    produto = get_object_or_404(Produtos, id=id)
    
    if request.method == "POST":
        produto.delete()
        messages.success(request, "Produto excluído com sucesso!")
        return redirect("index")
    
    context = {"produto": produto}
    return render(request, "excluir_produto.html", context)