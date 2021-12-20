from random import randint

def conta_vogais(st):
    qtde = 0
    vogais = "aeiou".upper()
    for i in range(len(st)):
        if (st[i].upper() in vogais):
            qtde += 1
    return qtde

def senha(qtde=10):
    st = ''
    for i in range(qtde):
        st += chr(randint(ord('A'), ord('Z')))
    return st

def exibir(palavra, memoria):
    for i in range(len(palavra)):
        if (palavra[i] in memoria):
            print(palavra[i], end=' ')
        else:
            print('_', end=' ')
    print()
