num = eval(input("digite o número inteiro a ser fatorado:"))

fat = num

for i in range(num,1,-1):

	calculo = fat*(i-1)

	fat = calculo

print()

print("o fatorial desse número é",fat)
