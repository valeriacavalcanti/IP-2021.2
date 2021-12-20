'''
2 elevado a 3 = 2 x 2 x 2 = 8
prodt=1
prodt=1*2=2
prodt=2*2=4

2 elevado a 4 = 2 x 2 x 2 x 2 = 16
'''
def potencia(x,y):
    prodt=1
    for i in range(y):
        prodt*=x
    return prodt

'''
programa principal
'''
print(potencia(2,4))
