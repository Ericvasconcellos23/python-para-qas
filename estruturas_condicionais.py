#Estruturas condicionais usando if, elif e else
idade = int(input('Qual a sua idade? '))

if idade >= 18:
     print('VOCÊ É DE MAIOR')

else:
    print('VOCÊ NÃO PODE PASSAR !')


nota1 = int(input('PRIMEIRA NOTA: '))
nota2 = int(input('SEGUNDA NOTA: '))
nota3 = int(input('TERCEIRA NOTA: '))
nota4 = int(input('QUARTA NOTA: '))
soma = nota1 + nota2 + nota3 + nota4
resultado = soma / 2

if soma >= 21:
     print('VOCÊ ESTÁ APROVADO ')

elif soma >= 10:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO ')

else:
    print('VOCÊ ESTÁ REPROVADO !')
