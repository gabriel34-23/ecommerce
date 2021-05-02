from django.db import models


class Categoria(models.Model):

    class Meta:

        db_table = 'categoria'

    Nome_Categoria = models.CharField(max_length=50)
    Codigo_Categoria = models.IntegerField()

    def __str__(self):
        return self.Nome_Categoria

class Produto(models.Model):

    class Meta:

        db_table = 'produto'

    Categoria_Produto = models.ForeignKey('Categoria', related_name='produtos', on_delete=models.CASCADE)
    Nome_Produto = models.CharField(max_length=50)
    descricao = models.TextField()
    Preco = models.DecimalField(max_digits=10, decimal_places=2)