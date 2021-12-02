from random import randint

# declarar a matriz
tam = int(input("Tamanho: "))
tabuleiro = []
for i in range(tam):
    tabuleiro.append([0]*tam)

# inserir as bombas
# bombas = int(input("Bombas: "))
# bombas = (tam * tam) // 3
bombas = randint(6, 10)
for i in range(bombas):
    #l, c = input("Local ({} e {}): ".format(tam-1, tam-1)).split()
    #l, c = int(l), int(c)
    tabuleiro[randint(0, tam-1)][randint(0, tam-1)] = -1

# inserir as pistas

for l in range(tam):
    for c in range(tam): # 0 até 9
        if (tabuleiro[l][c] != -1):
            # analisar as linhas
            if (c - 1 >= 0) and (tabuleiro[l][c - 1] == -1):
                tabuleiro[l][c] += 1
            if (c + 1 < tam) and (tabuleiro[l][c + 1] == -1):
                tabuleiro[l][c] += 1

            # analisar as colunas
            if (l - 1 >= 0) and (tabuleiro[l - 1][c] == -1):
                tabuleiro[l][c] += 1
            if (l + 1 < tam) and (tabuleiro[l + 1][c] == -1):
                tabuleiro[l][c] += 1

            # analisar as diagonais superiores
            if (l - 1 >= 0):
                if (c - 1 >= 0) and (tabuleiro[l - 1][c - 1] == -1):
                    tabuleiro[l][c] += 1
                if (c + 1 < tam) and (tabuleiro[l - 1][c + 1] == -1):
                    tabuleiro[l][c] += 1

            # analisar as diagonais inferiores
            if (l + 1 < tam):
                if (c - 1 >= 0) and (tabuleiro[l + 1][c - 1] == -1):
                    tabuleiro[l][c] += 1
                if (c + 1 < tam) and (tabuleiro[l + 1][c + 1] == -1):
                    tabuleiro[l][c] += 1

# testes
print('Estimativa de bombas:', bombas)
# imprimir o tabuleiro
for i in range(tam):
    print(tabuleiro[i])
