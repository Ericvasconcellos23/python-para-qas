# Ordenando listas com sort() e sorted()

# # sort() - Altera a lista original
# status_code = [200, 201, 400, 500, 404]
# status_code.sort()
# print(status_code)
#
# status_code.sort(reverse=True)
# print(status_code)

# Sorted() - retorna uma NOVA lista (original intacta)

# endpoints = ["/usuarios", "/login", "/produtos", "/logout"]
# print(sorted(endpoints))
# print(endpoints)

# Contagem, Busca e Inversão

# contagem usando count()

# resultados = ["PASSOU", "FALHOU", "PASSOU", "PASSOU", "FALHOU", "FALHOU",]
#
# print(resultados.count("PASSOU"))
# print(resultados.count("FALHOU"))
#
# # Posição da primeira ocorrência usa o index()
# print(resultados.index("FALHOU"))
#
# # Inverte a ordem usando reverse()
# etapas = ["login", "busca", "carrinho", "pagamento"]
# print(etapas)
# etapas.reverse()
# print(etapas)

# Copiando, Limpando e Combinando listas

# Copianddo usando copy()
# usuarios = ["lua@email.com", "maria@email.com"]
# copia = usuarios.copy()
# copia.append("joao@email.com")
#
# print(usuarios)
# print(copia)

# Limpando a lista usando clear()

# logs = ["log1", "log2", "log3"]
#
# logs.clear()
#
# print(logs)

# Combinando listas usando extend ()
# ambientes_br = ["dev-br", "html-br"]
# ambientes_us = ["dev-us", "html-us"]
# ambientes_br.extend(ambientes_us)
# print(ambientes_br)


# Juntar itens em uma única String join()
# campos = ["nomes", "emails", "senha"]
# print(" - ".join(campos))

# Quebra a String usando um separador split()

# csv_linha = "200,ok,120ms"
# valores = csv_linha.split(",")
# print(valores)

# Definindo um valor apenas se esse não exitir usando setdefault()

# usuario = {
#     "nome": "Carlos",
#     "idade": 30
# }
#
# print(usuario)
# usuario.setdefault("perfil", "viewer") # Adiciona
# usuario.setdefault("nome", "Outro") # NÃO sobrescreve
# print(usuario)
#

# Adicionando e sobrescrevendo utilizando update()

# usuario = {
#     "nome": "Carlos",
#     "idade": 30
# }
#
# print(usuario)
#
# usuario.update({"cidade": "Curitiba",  "idade": 18})
# print(usuario)

# Conversão entre estruturas

# Lista -> Set -> Lista ( remover duplicatas )
# ids = [101, 102, 103, 101, 102]
# ids_unicos = list(set(ids))
# print(ids_unicos)

# Listas de tuplas -> Dict
# pares = [("nome", "Ana"), ("perfil", "admin")]
# print(dict(pares))

# Dict -> Listas de tuplas
config = {"timeout": 30, "retries": 3}
print(list(config.items()))

