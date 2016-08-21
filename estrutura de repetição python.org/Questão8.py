n1 = eval(input("digite um número:"))
n2 = eval(input("digite outro número:"))
n3 = eval(input("digite outro número:"))
n4 = eval(input("digite outro número:"))
n5 = eval(input("digite outro número:"))
soma = 0
média = 0
for i in range(n1,n5+1):
	s = soma + i
	soma = s
print("a soma é",soma)