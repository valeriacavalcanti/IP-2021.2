matriz = []

for i in range(12):
    matriz.append([0]*12)

st = input()
for i in range(12):
    for j in range(12):
        # uDebug
        matriz[i][j] = float(input()) # 144

print(st)
print(matriz)
