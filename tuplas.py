# Criando tuplas

# Ambientes de testes fixos
# ambientes = ("Desenvolvimento", "Homologação", "Produção")
#
# # Códigos HTTP de sucesso esperados
# codigos_sucesso = (200, 201, 204)
#
# # Tipos mistos
# dados_misto = ("QA", 3, True)

# Para acessar os objetos nas tuplas

# ambientes = ("Desenvolvimento", "Homologação", "Produção")
#
# print(ambientes[0])
# print(ambientes[1])
# print(ambientes[2])
# print(ambientes[-1])

# Tuplas são imutáveis ( Não podem mudar ou ser alterada)

# ambientes = ("Desenvolvimento", "Homologação", "Produção")
#
# ambientes[1] = "Cabide" # Tentativa de alteração

# Usando lista - risco de alteração acidental

# urls = ["https://dev.api.com", "https://hml.api.com", "https://api.com"]
# urls[2] = "http://api.com" # Alteração silenciosa,  sem erro

# Usando Tupla - Protegida contra alteração

# urls = ("https://dev.api.com", "https://hml.api.com", "https://api.com")
# urls[2] = "http://api.com" # TyperError imediato
#
# print(urls)
# print(urls[2])

# Percorrer uma Tupla e Descobrir o tamanho

# codigos_sucesso = (200, 201, 204)
# print(len(codigos_sucesso))
#
# for codigo in codigos_sucesso:
#     print(f"Validando: {codigo}")

# Usando enumerate

ambientes = ("Desenvolvimento", "Homologação", "Produção")

for i, ambientes in enumerate(ambientes):
    print(f"{i + 1}. {ambientes}")