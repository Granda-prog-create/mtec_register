from django.shortcuts import render, redirect
from django.contrib.auth import logout
from produtos.models import Produtos

def index(request):
    todos_produtos = Produtos.objects.all()
    context = {"nome_pagina": "Seu estoque", "todos_produtos": todos_produtos}
    return render(request, "index.html", context)

def user_logout(request):
    logout(request)
    return redirect('login')
