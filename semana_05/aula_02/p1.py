'''
1.	Faça um programa que leia 3 números inteiros (N, X, Y)
 e mostre todos os números múltiplos de N entre X e Y.
 (Considere: X e Y maiores do que N e X < Y)

entrada
n=2
x=10
y=20

processamento
[11, 12, 13, 14, 15, 16, 17, 18, 19]

saida
12 14 16 18
'''

n=int(input('N: '))
x=int(input('X: '))
y=int(input('Y: '))
for i in range(x+1,y):
    if (i%n==0):
        print(i)


