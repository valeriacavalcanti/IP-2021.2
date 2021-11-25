numeros = [0] * 10
qtde = 0

# ler os valores
for i in range(10):
    numeros[i] = int(input('Número: '))

print(numeros)

# exibir os pares
for i in range(10):
    if (numeros[i] % 2 == 0):
        print(numeros[i])

# quantidade de valores iguais ao último
for i in range(9): # 0 1 2 3 4 5 6 7 8
    if (numeros[i] == numeros[9]):
        qtde += 1

print(qtde)
print(numeros.count(numeros[9]) - 1)
print(numeros[0:9].count(numeros[9]))
