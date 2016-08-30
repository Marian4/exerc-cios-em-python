base = eval(input("Base:"))

expoente = eval(input("expoente:"))

resultado = base

for i in range(expoente-1):

	calculo = resultado*base

	resultado = calculo

print(base,'elevado a',expoente,'é igual a',resultado)