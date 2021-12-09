frase = input('Frase: ')
print(frase)

# exibir com espaçamento - 4
for i in range(len(frase)): # 0 1 2 3 ...
    print(frase[i], end=' ' * 4)

print()

# exibir ao inverso
for i in range(len(frase) - 1, -1, -1): #
    print(frase[i], end= '')
