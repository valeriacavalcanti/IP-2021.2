numeros = []

num = int(input('Número: '))
while (num != 0):
    # verificar se ele existe, se não existir -- append!
    if (num not in numeros):
        numeros.append(num)
    num = int(input('Número: '))

print(numeros)
