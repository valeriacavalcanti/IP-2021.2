def somar(conjunto):
    total = 0
    for i in range(len(conjunto)):
        total += conjunto[i]
    return total

def media(conjunto):
    return somar(conjunto)/len(conjunto)

def acima_media(conjunto):
    acima = []
    valor = media(conjunto)
    for i in range(len(conjunto)):
        if (conjunto[i] > valor):
            acima.append(conjunto[i])
    return acima
