from django import forms
from produtos.models import Produtos

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = "__all__"
        error_messages = {
            "nome_produto": {"required": "O nome do produto é obrigatório para o registro!"},
            "valor_produto": {"required": "O valor é obrigatório para o registro!"},
            "data_venda": {"required": "A data da venda é obrigatória para o registro!", "invalid": "Favor informar um formato válido! (DD/MM/AAAA)" },
        }

class AutorizaVendaForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = [
            "vendedor_responsavel"
        ]  
        error_messages = {
            "vendedor_responsavel": {
                "required": "Por favor, informe o nome do vendedor responsável" 
            }
        }
