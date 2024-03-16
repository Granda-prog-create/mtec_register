#Formulários de cadastro
from django import forms
from produtos.models import Produtos

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = "__all__"