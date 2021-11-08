soma = 0

qtde = int(input('Quantidade: '))

# quero repetir qtde vezes
# for i in range(1, qtde + 1):
for i in range(qtde):
    num = int(input("Número {}: ".format(i + 1)))
    soma = soma + num

media = soma / qtde

print('soma =', soma)
print('Média =', media)
