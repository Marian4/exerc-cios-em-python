print("forneça um conjunto com 10 números")

print()

n1 = eval(input("digite o primeiro número:"))

while n1 > 100 or n1 <= 0:

	print("esse número está fora dos limites impostos!")

	n1 = eval(input("digite o primeiro número:"))

maior = n1

menor = n1

for i in range(9):

    n = eval(input("digite o próximo número:"))

    while n > 100 or n <= 0:

    	print("esse número está fora dos limites impostos!")

    	n = eval(input("digite o próximo número:"))

    if maior < n:

    	maior = n

    if menor > n:

    	menor = n

print()

print("o maior número é o número",maior)

print()

print("o menor número é o número",menor)

soma = maior + menor

print()

print("a soma do maior número com o menor é igual a",soma)
