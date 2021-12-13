def escopo():
    # variável de escopo: local
    tam = 10
    print("função escopo")

def variaveis():
    qtde = 20
    print('Função:', qtde)

def incrementar():
    global qtde
    qtde += 1

# PROGRAMA PRINCIPAL
# variáveis de escopo: global
qtde = 10

escopo()
variaveis()
print('Principal:', qtde)

incrementar()
print('Principal:', qtde)
