# # Laços aninhados são loops dentro de outros loops
# # Exemplo com for
# for linhas in range(5):
#     for colunas in range(6):
#         print("*", end=" ")
#     print()

# Exemplo com while ( não é tão comum)
# i = 0
#
# while i < 3:
#     j = 0
#
#     while j < 4:
#         print("i =", i, "| j =", j)
#         j += 1
#
#     i += 1

# Aplicação prática para QA
usuarios = ["Ana", "Carlos"]

for usuario in usuarios:
    for tentativa in range(6):
        print("Testando login de", usuario, "= tentativa", tentativa)

if tentativa <=3:
    print("Login aceito")

else:
    print('Login incorreto')