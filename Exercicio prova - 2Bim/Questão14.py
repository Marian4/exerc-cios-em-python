n = eval(input("digite um número:"))
n2 = eval(input("digite outro número:"))
n3 = eval(input("digite outro número:"))
n4 = eval(input("digite outro número:"))
n5 = eval(input("digite outro número:"))
n6 = eval(input("digite outro número:"))
n7 = eval(input("digite outro número:"))
n8 = eval(input("digite outro número:"))
n9 = eval(input("digite outro número:"))
n10 = eval(input("digite outro número:"))
lista = [n,n2,n3,n4,n5,n6,n7,n8,n9,n10]
print("números pares:")
for i in range(lista[0],lista[9]+1):
	if i%2 == 0 :
		print(i)
print("números impares:")
for j in range(lista[0],lista[9]+1):
	if j%2 == 1 :
		print(j)
