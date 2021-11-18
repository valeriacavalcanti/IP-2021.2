
#loop infinito

soma = qtde = 0

while(True):
    num = int(input('Número: '))

    if (num == 0):
        break

    soma += num
    qtde += 1

print(qtde)
print(soma)
