from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^produtos/$', views.ProdutoLista.as_view()),

]


