def peso_ideal(alt,sexo):
    if sexo=='F':
        pideal=62.1 * alt - 44.7
    else:
        pideal=72.7 * alt - 58
    return pideal

# programa principal

alturap=float(input("informe a altura: "))
sexop=input("informe o sexo (F/M): ")
peso=peso_ideal (alturap,sexop.upper())
print ('Peso ideal: ', peso)
