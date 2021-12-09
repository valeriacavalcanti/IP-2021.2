# converter para maiúsculo
# -32

letra = input('Letra: ')

if (letra >= 'a') and (letra <= 'z'):
    # tirar 32 e exibir o símbolo
    print(chr(ord(letra) - 32))
else:
    # print('nao é uma letra minúscula')
    print(letra)

# ---------------------------------

print(letra.upper())
