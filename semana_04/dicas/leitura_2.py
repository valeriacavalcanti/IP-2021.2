# ler 03 (três) números, no mesmo input!

# o comando "split" quebra a string com as informações do usuário em substrings
# o critério padrão utilizado para essa quebra é o "espaço em branco"
# (esse critério pode ser substituído, vamos ver isso nas próximas semanas)

# uma vez que são 03 (três) valores, serão geradas 03 (três) substrings
# cada uma vai ficar armazenada em sua respectiva variável

num1, num2, num3 = input().split()

# agora é só fazer a conversão dos tipos (str para int)

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

print(type(num1), num1)
print(type(num2), num2)
print(type(num3), num3)
