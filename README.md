# teste_e_commerce

Primeiro passo é a criação do usuario através do comando

python manage.py createsuperuser

Após a criar o usuario start o servidor com o comando

python manage.py runserver

Depois Acesse o link:

http://127.0.0.1:8000/admin/

Faça o login, a parti daí o usuario mestre terá acesso aos dados do sistema

Para acessar a api, digite a seguinte url no navegador
http://127.0.0.1:8000/produtos/

Nesta tela o usuario poderá ver às propriedades e funções de GET, POST 

Para deletar e alterar basta colocar os seguintes comandos no terminal 

Deletar: curl -X DELETE http://127.0.0.1:8000/produtos/ -H 'content-type: application/json' -d '{"title": "É o amor", "seconds": 305}'

Alterar: curl -X PUSH http://127.0.0.1:8000/produtos/ -H 'content-type: application/json' -d '{"title": "É o amor", "seconds": 305}'
