# Utilizando FOR para percorrer uma lista
# status_code = [200, 404, 400, 500, 201, 403]
#
# for code in status_code:
#     if code >= 400:
#         print(f"Status {code}: ERRO")
#     else:
#         print(f"Status {code}: OK")


# ZIP(): Combinar Estruturas em Paralelo

testes = ["Login", "Busca", "Checkout"]
resultados = ["PASSOU", "FALHOU", "PASSOU"]

for teste, resultado in zip(testes, resultados):
    print(f"{teste}: {resultado}")
