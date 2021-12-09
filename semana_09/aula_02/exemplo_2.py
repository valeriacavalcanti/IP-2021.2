# procurar uma letra na string

frase = input('Frase: ')
letra = input('Letra: ')

posicao = -1
qtde = 0
existe = False
for i in range(len(frase)):
    if (frase[i] == letra):
        posicao = i
        qtde += 1
        existe = True
        break

# valeria
if (posicao != -1):
    print('tem')
else:
    print('não tem')

# ícaro
if (qtde == 0):
    print("nao tem")
else:
    print('tem')

# Crishane
if (existe == True):
    print('tem')
else:
    print('nao tem')

# -------------------------------

print(frase.find(letra))
