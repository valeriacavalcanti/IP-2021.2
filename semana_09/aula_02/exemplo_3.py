# contar letras em uma string

frase = input('Frase: ')
letra = input('Letra: ')

qtde = 0

for i in range(len(frase)):
    if (frase[i] == letra):
        qtde += 1

print(qtde)

# -------------------------------

print(frase.count(letra))
