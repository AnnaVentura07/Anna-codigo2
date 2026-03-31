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

