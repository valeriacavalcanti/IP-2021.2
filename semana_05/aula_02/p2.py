'''
2.	Faça um programa que, para um grupo de N pessoas
(obs: N será lido):
•	Leia a altura de cada pessoa;
•	Calcule e mostre a altura média do grupo;
•	Calcule e mostre a maior altura informada


entrada
n=5

alturas lidas=[1.65, 1.76, 1.80, 1.67, 1.64]
processamento
soma=0
soma=soma+1.65=1.65
soma=soma+1.76=3.41
soma=soma+1.80=5.21
...
soma=8.52

media=soma/n
media=1.70

saida
altura media = 1.70
maior altura = 1.80
'''

soma=0
maior=0
n=int(input('N: '))
for i in range(n):
    altura=float(input('Altura: '))
    soma=soma+altura
    if (altura>maior):
        maior=altura
media=soma/n
print('altura media = {:.2f}'.format(media))
print('maior altura = {:.2f}'.format(maior))
