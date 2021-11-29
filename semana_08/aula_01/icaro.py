notas = []

# declarar a matriz
for i in range(16):
    notas.append([0]*4)

# TODOS terão nota 100

# 16 linhas
for i in range(16): # 0 1 2 3 4 ... 16
    for j in range(4): # 0 1 2 3
        print(i, j)
        notas[i][j] = int(input())

for i in range(16):
    print(notas[i])
