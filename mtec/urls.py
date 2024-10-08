from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import index, user_logout
from produtos.views import (registar_produto, informacoes_produto, finalizar_venda, editar_produto, excluir_produto, produtos_recebidos, produtos_estoque, vendas_mes_atual)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),

    path("logout/", user_logout, name="logout"),

    path("", index, name="index"),

    path("registrar-produto/", registar_produto, name="registrar_produto"),

    path("produtos/<int:id>/", informacoes_produto, name="informacoes_produto"),

    path("vendas/<int:id>/finalizar-venda", finalizar_venda, name="finalizar_venda"),

    path("produtos/<int:id>/editar-produto", editar_produto, name="editar_produto"),

    path("produtos/<int:id>/excluir-produto", excluir_produto, name="excluir_produto"),

    path("produtos-recebidos/", produtos_recebidos, name="produtos_recebidos"),

    path("produtos-estoque/", produtos_estoque, name="produtos_estoque"),

    path("vendas-mes-atual/", vendas_mes_atual, name="vendas_mes_atual"),
]