n = eval(input("digite um n�mero:"))
n2 = eval(input("digite outro n�mero:"))
n3 = eval(input("digite outro n�mero:"))
n4 = eval(input("digite outro n�mero:"))
n5 = eval(input("digite outro n�mero:"))
n6 = eval(input("digite outro n�mero:"))
n7 = eval(input("digite outro n�mero:"))
n8 = eval(input("digite outro n�mero:"))
n9 = eval(input("digite outro n�mero:"))
n10 = eval(input("digite outro n�mero:"))
lista = [n,n2,n3,n4,n5,n6,n7,n8,n9,n10]
print("n�meros pares:")
for i in range(lista[0],lista[9]+1):
	if i%2 == 0 :
		print(i)
print("n�meros impares:")
for j in range(lista[0],lista[9]+1):
	if j%2 == 1 :
		print(j)