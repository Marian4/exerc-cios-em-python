print("forne�a um conjunto com 10 n�meros")

print()

n1 = eval(input("digite o primeiro n�mero:"))

maior = n1

menor = n1

for i in range(9):

    n = eval(input("digite o pr�ximo n�mero:"))

    if maior < n:
 
    	maior = n

    if menor > n:

    	menor = n

print()
print("o maior n�mero � o n�mero",maior)

print()

print("o menor n�mero � o n�mero",menor)

soma = maior + menor

print()

print("a soma do maior n�mero com o menor n�mero � igual a",soma)