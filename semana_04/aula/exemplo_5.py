# parcelamento
# [0, 100] - não divive
# ]100,150] - 2 parcelas
# ]150, 200] - 3 parcelas
# ]200, ...[ - 4 parcelas

valor = float(input('Valor: '))

if (valor <= 100):
    print('nao divide')
else:
    # valor > 100 - passou por aqui
    if (valor <= 150):
        print('2 parcelas')
        print(valor/2)
    else:
        # valor > 150
        if (valor <= 200):
            print('3 parcelas')
            print(valor/3)
        else:
            # valor > 200
            print('4 parcelas')
            print(valor/4)
