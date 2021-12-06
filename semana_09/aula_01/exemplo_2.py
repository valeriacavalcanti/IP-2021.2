# ler frase
# quantas letras minúsculas?
# quantas letras maiúsculas
# quantos símbolos numéricos

qtdeMin = qtdeMai = qtdeNum = qtdeEsp = 0
frase = input('Frase: ')

for i in range(len(frase)):
    if (ord(frase[i]) >= 97 and ord(frase[i]) <= 122):
        qtdeMin += 1
    elif (ord(frase[i]) >= 65 and ord(frase[i]) <= 90):
        qtdeMai += 1
    elif (ord(frase[i]) >= 48 and ord(frase[i]) <= 57):
        qtdeNum += 1
    else:
        qtdeEsp += 1

print(len(frase))
print(qtdeMin)
print(qtdeMai)
print(qtdeNum)
print(qtdeEsp)
