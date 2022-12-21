# Importar bibliotecas necessárias
import csv

# Definir a lista de produtos e preços
produtos = [
    {"nome": "produto 1", "preco": 10.99},
    {"nome": "produto 2", "preco": 15.50},
    {"nome": "produto 3", "preco": 22.99},
]

# Pedir ao usuário para informar o produto desejado
produto_desejado = input("Informe o nome do produto desejado: ")

# Pesquisar o preço do produto desejado
preco_encontrado = None
for produto in produtos:
    if produto["nome"] == produto_desejado:
        preco_encontrado = produto["preco"]
        break

# Exibir o preço do produto desejado
if preco_encontrado is not None:
    print("O preço do produto é:", preco_encontrado)
else:
    print("Produto não encontrado.")

