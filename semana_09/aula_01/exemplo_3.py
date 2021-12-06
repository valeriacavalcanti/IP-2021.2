# ler frase
# quantas letras minúsculas?
# quantas letras maiúsculas
# quantos símbolos numéricos

qtdeMin = qtdeMai = qtdeNum = qtdeEsp = 0
frase = input('Frase: ')

for i in range(len(frase)):
    if (frase[i] >= 'a' and frase[i] <= 'z'):
        qtdeMin += 1
    elif (frase[i] >= 'A' and frase[i] <= 'Z'):
        qtdeMai += 1
    elif (frase[i] >= '0' and frase[i] <= '9'):
        qtdeNum += 1
    else:
        qtdeEsp += 1

print(len(frase))
print(qtdeMin)
print(qtdeMai)
print(qtdeNum)
print(qtdeEsp)
