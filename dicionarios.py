# Criando um dicionário

# Printando só as chaves (Keys) e os valores (Values)

# usuario={
#     "nome":"Maria",
#     "idade":25,
#     "ativo":True
# }
#
# print(usuario)

# Chamando um valor específico, só printar a variável e [valor]

# usuario={
#     "nome":"Maria",
#     "idade":25,
#     "ativo":True
# }
#
# print(usuario["idade"])

# Adicionando um valor a um dicionário

# usuario={
#     "nome":"Maria",
#     "idade":25,
#     "ativo":True,
# }
#
# usuario ["cidade"] = "Rio de Janeiro"
# print(usuario["cidade"])

# Alterando valores em um dicionário

# usuario={
#     "nome":"Maria",
#     "idade":25,
#     "ativo":True
# }
#
# usuario ["ativo"] = False
# print(usuario)

# Removendo um elemento em um didionário usa o pop()

# usuario={
#     "nome":"Maria",
#     "idade":25,
#     "ativo":True
# }
#
# usuario.pop("idade")
# print(usuario)

# Percorrendo um dicionário usando for

# usuario={
#     "nome":"Maria",
#     "idade":25,
#     "ativo":True
# }
#
# for chave, valor in usuario.items():
#     print( chave, valor)

# Aplicação prática para QAs

resposta_api= {
    "status_code": 200,
    "mensagem": "Sucesso",
    "tempo_resposta": 120
}

if resposta_api["status_code"] != 200:
    print("Erro na API")

else:
    print("tempo de resposta: ",resposta_api["tempo_resposta"])