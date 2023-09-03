# Ex4-Python
Exercicio 4, banco_usuarios

Aluno:Felipe Porto Caldeira do Nascimento

Como Utilizar:

O usuario deve definir no minimo 1 campo obrigatorio, sendo esse o "nome", pois o usuario esta cadastrando usuarios.
Apos definir os campos obrigatorios, o programa inicia. 

Se o usuario escolher a opcao 1, o programa ira pedir para preencher os campos obrigatorios e então,
irá perguntar se o usuario deseja registrar campos opcionais especificos para o usuario que está sendo registrado.
Basta digitar 'sair' para voltar ao menu principal.

Se o usuario escolher a opcao 2, ele tera 4 opções
1 - impirmir todos
2- filtrar por nomes
3- filtrar por campos
4 - filtrar por nomes e campos

Imprimir todos irá mostrar todos usuarios registrado no BD.

Filtrar por nomes ira mostrar todos os usuarios com um nome informado.

Filtrar por campos ira mostrar todos os usuarios com um campo especifico.

Filtrar por nomes e campos ira mostrar todos os usuarios entre x y z com campos especificos.

Exemplo:


campos obrigatorios: nome,idade

Usuarios registrados:

>>>>>nome: Felipe

>>>>>idade: 18

campo opcional: cidade

>>>>>nome: Alexandre

>>>>>idade: 19

>>>>>cidade: Curitiba

nome: Gustavo
idade: 20


>>>>>4 - filtrar por nomes e campos

Digite nomes separados por ',' para filtrar por nomes: Felipe,Alexandre,Gustavo

Digite campos para busca separados por ',' (exemplo: nome,idade): cidade

Digite um valor para cidade: Curitiba

>>>>>{'nome': 'Alexandre', 'idade': '19', 'cidade': 'Curitiba'}
