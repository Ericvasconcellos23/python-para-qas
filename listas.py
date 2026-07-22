# ambientes = ["Maria Eduarda", "Luana Ribeiro", "Alex Souto"]
from operator import index

# print(ambientes[-1])
# print(ambientes[1])
# print(ambientes[2])

# Indices negativos usamos o sinal de menos (-)

# print(ambientes[-1])
# print(ambientes[-2])
# print(ambientes[-3])

# execucoes = ["Teste passou", "Teste falhou", "Teste passou", "Teste Falhou"]
#
# ultimo_resultado = execucoes[-2]
# print(ultimo_resultado)

# Modificando um índice

# usuarios = ["maria.gomes@123.com", "joao.cbris@123.com", "pedro.feliz@123.com"]
#
# print(usuarios)
#
# usuarios [1] = "joao.cabris@123.com"
#
# print(usuarios)

# Adicionando usuarios no final da lista com append

# usuarios = ["Carla", "joaquim"]
# print(usuarios)
# usuarios.append("Manoela")
# usuarios.append("Pedro")
# print(usuarios)

# Adicionando usuarios em qualquer lugar da lista
# usuarios = ["Carla", "joaquim"]
#
# usuarios.insert(index(3),"pedro")
# usuarios.insert(1, "camila")
# print(usuarios)

# Removendo elementos da lista com remove

# usuarios = ["Carla", "Joaquim", "Pedro", "Manoela"]
#
# usuarios.remove("Manoela")
# print(usuarios)

# Removendo elementos da lista com pop, se não informar o índice
# ele remove sempre o último elemento da lista.
# usuarios = ["Carla", "Joaquim", "Pedro", "Manoela"]
# print(usuarios)
# removendo = usuarios.pop()
# print(f"Usuário removido: {removendo}" )
# print(f"Lista atualizada: {usuarios}" )

# Cenário: Validar se o número de resultados retornados pela API está correto

# resultados_api = ["item1", "item2", "item3", "item4", "item5", "item6", "item7"]

# total = len(resultados_api)
#
# print(f"Total de resultados:{total}")
#
# esperado = 6
#
# if total  == esperado:
#     print("Quantidade de resultados correta !")
#
# else:
#     print(f"Esperava {esperado}, mas veio {total} resultados")


# Cenário: Imprimitr todos os ambientes disponíveis para teste

# ambientes_disponiveis = ["desenvolvimento", "homologação", "objeto", "API"]

# for ambiente in ambientes_disponiveis:
#     print(f"testando em: {ambiente}")

# ambientes_disponiveis = ["desenvolvimento", "homologação", "objeto", "API"]
#
# for i, v in enumerate(ambientes_disponiveis):
#     print(f"caso {i +1} : {v}")

# Cenário: Verificar se o Status Code retornado é um dos esperados utilizando IN

# codigos_sucesso = [200, 201, 204]
#
# codigo_recebido = 401
#
# if codigo_recebido in codigos_sucesso:
#     print(f"Código {codigo_recebido} é um códgio de sucesso")
#
# else:
#     print(f"{codigo_recebido} inválido!")


# Cenário: Verificar se o Status Code retornado é um dos esperados utilizando NOT IN
erros_crticos = [500, 502, 503]

codigo = 500

if codigo not in erros_crticos:
    print(f"Código {codigo} é um códgio de sucesso")
