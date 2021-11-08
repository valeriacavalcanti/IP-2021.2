soma = 0

# quero repetir 10 vezes
for i in range(1,11):
    num = int(input("Número {}: ".format(i)))
    soma = soma + num

media = soma / 10

print('soma =', soma)
print('Média =', media)
