# Estruturas de repetição (for, while)
for numero in range(10):
    print(numero)

contador = 0

while contador < 15:
    print(contador)
    contador += 1

tentativas = 0

while tentativas < 3:
    print('Tentando login...')
    tentativas += 1

numero = 0
while numero < 10:
    print(numero)
    if numero == 5:
        break

    numero += 1

for contador in range(14):
    if contador == 5:
        break
    print(contador)

#Utilizando o continue
#
for contador in range (12):
    if contador == 8:
        continue
    print(contador)

contador = 0

while contador < 10:
    contador += 1
    if contador == 6:
        continue
    print(contador)

#Utilizando em uma situação real

status_code = [200, 404, 500, 200]

for i in status_code:
    if i == 400:
        print(f"status: {i}, Erro encontrado")
        break

else:
    print('TUDO NORMAL NO SISTEMA')





