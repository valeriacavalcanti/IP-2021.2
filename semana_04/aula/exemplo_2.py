# aprovado
# média maior ou igual a 70
# frequencia maior ou igual a 75

# and: tudo tem que ser True
# or: é suficiente que no mínimo um seja True

media = int(input('Média: '))
freq = int(input('Frequencia: '))

if (media >= 70) and (freq >= 75):
    print('aprovado')
else:
    print('reprovado')
