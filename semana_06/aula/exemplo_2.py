# ler vários números!!! encerrar quando for informado
# número 0 (zero).

# exiba:
# - soma dos números lidos
# - média dos números lidos

soma = 0
qtde = 0

num = int(input('Número: '))# PRIMEIRO
while (num != 0):
    soma += num
    qtde += 1
    num = int(input('Número: ')) #PRÓXIMOS

if (qtde > 0):
    media = soma/qtde
    print('\nMEMÓRIA')
    print('num:', num) # sempre vai exibir zero
    print('soma:', soma)
    print('qtde:', qtde)
    print('media:', media)
else:
    print('Nenhum valor digitado')
