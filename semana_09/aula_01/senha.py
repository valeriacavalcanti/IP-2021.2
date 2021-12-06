# 65 - 90
from random import randint

senha = ''
for i in range(10):
    senha = senha + chr(randint(65, 90))

print(senha)
