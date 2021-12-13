from random import randint

# Funções
# Função exibir a lista, recebe por p
def print_lista(qtde, pLista):
    print('-'*10, 'Início', '-'*10)
    if (qtde > len(pLista)):
        qtde = len(pLista)
    for i in range(qtde):
        print(i, pLista[i])
    print('-'*10, 'Fim', '-'*10)


# PROGRAMA PRINCIPAL

# gerando a lista
numeros = [0] * 6

# imprimindo a lista
print_lista(6, numeros)

# atribuindo valores aleatórios
for i in range(6):
    numeros[i] = randint(1,60)

# imprimindo a lista
print_lista(3, numeros)

# ordenando a lista
numeros.sort()

# imprimindo a lista
print_lista(4, numeros)

print_lista(10, numeros)
