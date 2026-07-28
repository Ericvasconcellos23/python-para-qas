import requests
import json

# # JSONPlaceholder: API publica gratuita para testes
#
# resposta = requests.get('https://jsonplaceholder.typicode.com/users/1')
# # dados = resposta.json()
#
# print(dados["name"])
# print(dados["email"])
# print(dados["id"])

# Lendo JSON de um arquivo com .json.load()

# with open("fixtures/usuario.json", encoding="utf-8") as f:
#     dados = json.load(f)
#
# print(dados["nome"])
# print(dados["ativo"])

# Dados com um json dentro de outro

# dados = json.loads("""
# {
#     "pedido": {
#         "id": "PED-1042",
#         "cliente": {"nome": "Danilo Louco", "email": "danilo@qa.com"},
#         "itens": [{"produto": "Notebook", "preco": 4500.00}]
#     }
#
# }"""
#
# )
#
# pedido = dados["pedido"]
# print(pedido["id"])
# print(pedido["cliente"]["nome"])
# print(pedido["itens"][0]["produto"])
# print(pedido["itens"][0]["preco"])

# Acessando campos com .get()

# dados = resposta.json()
#
# # com []: levanta KeyError se o campo não exixtir
# # dados["email"] -> KeyError!
#
# # com .get(): retorna None sem erro
# email = dados.get('email')
# perfil = dados.get('perfil', 'sem perfil')
#
# print(email)
# print(perfil)

# Salvando JSON em Arquivo com json.dump()

fixture = {
    "id": 10,
    "nome": "Barbara Loureiro",
    "email": "barbara@qa.com",
    "ativo": True,
    "permissoes": ["ler", "escrever", "publicar"]

}

with open("fixtures/usuarios.json", "w", encoding="utf-8") as f:
    json.dump(fixture, f, ensure_ascii=False, indent=4)

