def divisores(n):
    lista=[]
    for i in range(1,n+1):
        if (n%i==0):
            lista.append(i)
    return lista
'''
 programa principal
'''
lista_divisores=divisores(6)
print(lista_divisores)

print('res nos print ',divisores(4))
