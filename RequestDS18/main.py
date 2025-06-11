import requests

id_personagem = input("Digite o nome do personagem:")

"""
Digite o ID para tratar no JSON
response = requests.get("http://ponyapi.net/v1/character/3")
"""

#Peço para o usuário digitar o id do personagem e puxo para coolocar o nome
#Colocar o f para conseguri puxar aquilo que o usuário digitar
response = requests.get(f"http://ponyapi.net/v1/character/{id_personagem}")

#Pego e coloco em JSON para manipular
personagem = response.json()

#índice 0 para pegar a informação do nome, já que temos duas listas dentro do dicionário
nome_personagem = personagem["data"][0]["name"]

print(nome_personagem)
