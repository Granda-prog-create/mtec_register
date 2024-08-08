from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import index, user_logout
from produtos.views import (registar_produto, informacoes_produto, finalizar_venda)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("login/", auth_views.LoginView.as_view(
        template_name="login.html"), 
        name="login"),

    path("logout/", user_logout, name="logout"), 

    path("", index, name="index"),


    path("registrar-produto/", registar_produto, name="registrar_produto"),  

    path("produtos/<int:id>/", informacoes_produto, name="informacoes_produto"),

    path("vendas/<int:id>/finalizar-venda", finalizar_venda, name="finalizar_venda"),
]


