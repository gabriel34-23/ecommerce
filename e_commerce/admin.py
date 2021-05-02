from django.contrib import admin
from .models import Produto
from .models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
	model =	Produto
	list_display = ('Nome_Categoria', 'Codigo_Categoria')
	search_fields = ['Nome_Categoria','Codigo_Categoria']


class ProdutoAdmin(admin.ModelAdmin):
	model =	Categoria
	list_display = ('Categoria_Produto', 'Nome_Produto', 'descricao', 'Preco')
	search_fields = ['Categoria_Produto','Nome_Produto', 'descricao', 'Preco']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)

