from random import  randint

def letra_maiuscula_aleatoria():
    return chr(randint(ord('A'), ord('Z')))

def palavra_maiuscula_aleatoria(qtde=6):
    st = ''
    for i in range(qtde):
        st += letra_maiuscula_aleatoria()
    return st

# PROGRAMA PRINCIPAL
print(letra_maiuscula_aleatoria())
print(palavra_maiuscula_aleatoria(8))
print(palavra_maiuscula_aleatoria(12))
print(palavra_maiuscula_aleatoria())
