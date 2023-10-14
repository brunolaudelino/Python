#Operdores Aritméticos
#Adição
print(1 +1)
#Subtração
print(10 - 2)
#Multiplicação
print(4 * 3)
#Divisão
print(12 / 3)
#Divisão inteira
print(12 // 2)
#Módulo
print(10 % 3)
#Exponenciação
print(2 ** 3)

#Operadores de Comparação
saldo = 450
saque = 200

#igualdade
print(saldo == saque)

#Diferença
print(saldo != saque)

#Maior que / Maior ou igual

print(saldo > saque)
print(saldo >= saque)

Menor que / Menor ou igual

print(saldo < saque)
print(saldo <= saque)
#Atibuição
saldo = 500
saldo += 200
saldo *= 5
print(saldo)

#Operadores Lógicos 
#and / E
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite 
>>> False

#Or / Ou
saldo= 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite 
>>> True

#Operadores de Identidade 

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso 
>>> false

#Operadores de Associação

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"python" in curso
>>> True

"maça" not in frutas
>>> True

200 in saques
>>> False