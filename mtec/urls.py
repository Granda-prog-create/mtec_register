#Registro de urls do projeto
from django.contrib import admin
from django.urls import path
from users.views import index
from produtos.views import registar_produto

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("registrar-produto/", registar_produto, name="registrar_produto"),  
]