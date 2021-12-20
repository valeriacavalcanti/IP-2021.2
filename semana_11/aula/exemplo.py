#import funcoes
#from funcoes import senha
#from funcoes import conta_vogais
#from funcoes import exibir
from funcoes import senha, conta_vogais, exibir

# PROGRAMA PRINCIPAL

#frase = input('Frase: ')
#frase = funcoes.senha(20)
frase = senha(20)
#qtde_vogais = funcoes.conta_vogais(frase)
qtde_vogais = conta_vogais(frase)
print(frase)
print('Quantidade de vogais:', qtde_vogais)

#funcoes.exibir('instituto', 'aeiout')
exibir('instituto', 'aeiout')

print("instituto federal da paraíba".split())
print("20/12/2021".split('/'))

print(senha())
