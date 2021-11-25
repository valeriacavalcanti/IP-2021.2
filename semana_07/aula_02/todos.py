numeros = [0]*6

for i in range(6): # 0 1 2 3 4 5
    numeros[i] = int(input('Número: '))

# exibir todos os números lidos
for i in range(6):
    print(i, numeros[i])

print('-'*12)

# exibir os números lidos na ordem inversa
for i in range(5, -1, -1): # 5 4 3 2 1 0
    print(i, numeros[i])
