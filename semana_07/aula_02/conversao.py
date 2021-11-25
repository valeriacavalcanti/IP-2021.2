numero = int(input('Número: '))
binario = []

while (numero // 2 != 0):
    binario.append(numero % 2)
    numero = numero // 2

binario.append(numero)
print(numero)
print(binario)

print(len(binario))

for i in range(len(binario) - 1, -1, -1):
    print(binario[i], end = '')
