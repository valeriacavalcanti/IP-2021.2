def nome_mes(n):
    mes=['janeiro','fevereiro','março','abril','maio',
         'junho','julho','agosto','setembro','outubro',
         'novembro','dezembro']
    return mes[n]

#programa principal

dia=int(input('dia: '))
mes=int(input('mes: '))
ano=int(input('ano: '))
print (dia,'de',nome_mes(mes-1), 'de', ano)
