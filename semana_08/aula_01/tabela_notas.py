notas = []

# declarar a matriz
for i in range(16):
    notas.append([0]*4)
'''
# imprimir a matriz
for i in range(16):
    print(notas[i])
'''
notas[0][0] = 88
notas[0][1] = 10
notas[0][2] = 2
notas[0][3] = 100
#print(type(notas[0]), notas[0])

# imprimir a matriz
for i in range(16):
    print(notas[i])
