# jogo da forca!

palavra = 'IFPB'
dica = 'Melhor instituição de ensino do mundo'

status = [False] * len(palavra)

print(status)
letra = 'f'

for i in range(len(palavra)):
    if (palavra[i]  == letra.upper()):
        status[i] = True

print(status)

for i in range(len(palavra)):
    if (status[i] == True):
        print(palavra[i], end=' ')
    else:
        print('_', end=' ')
