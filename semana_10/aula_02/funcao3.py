def media(listat):
    soma=0
    for i in range(len(listat)):
        soma+=listat[i]
    med=soma/len(listat)
#    print('media: ', med)
    return med

# verifica num dias acima da media de temperatura
def temp(lista):
    m=media(lista)
    qtd=0
    for i in range(len(lista)):
        if lista[i]>m:
            qtd+=1
    return qtd,m

# programa principal

temperaturas=[35,23,12,40,15,21]
dias_acima_media,temp_media=temp(temperaturas)
print ('temperaturas: ', temperaturas)
print('temp media: ', temp_media)
print('Dias acima media: ', dias_acima_media)
