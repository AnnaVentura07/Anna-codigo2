# Documentação da API: Gestão de Produtos

Este projeto é uma API desenvolvida em Flask para gerenciar um catálogo de produtos.  
A principal melhoria foi a organização do banco de dados utilizando o **Flask-SQLAlchemy**, deixando o código mais limpo e fácil de manter.

---

## O que este projeto faz

A API permite cadastrar, listar e remover produtos.  
Em vez de usar comandos SQL complexos, agora trabalhamos diretamente com objetos Python, tornando o desenvolvimento mais fluido e seguro.

---

## Configuração do Ambiente

Para rodar o projeto em sua máquina, instale as bibliotecas necessárias com o comando:

```bash
pip install flask flask-sqlalchemy

## Como usar a API

Após iniciar o servidor com:

```bash
python app.py

Você pode interagir com as seguintes rotas:

Lista de itens
Caminho: /produtos
Método: GET
Resultado: Retorna uma lista com todos os produtos cadastrados no sistema.
Cadastro de novo produto
Caminho: /produtos
Método: POST
Formato: JSON contendo nome e preço
Resultado: O produto é salvo no banco e retorna os dados do item criado.
Remoção de produto
Caminho: /produtos/<id>
Método: DELETE
Resultado: Remove o item específico do banco de dados usando o ID.
Organização do Código

O projeto foi estruturado para separar responsabilidades:

Configuração: Define onde o banco de dados será salvo.
Modelos: Representações das tabelas do banco via SQLAlchemy.
Rotas: Endpoints da API para cadastro, listagem e exclusão de produtos.
Execução: Arquivo principal app.py para iniciar o servidor.
Observações
A API pode ser expandida com autenticação, validação de dados e filtros avançados.
Ideal para projetos pequenos ou aprendizado de Flask + SQLAlchemy.
