N = eval(input("digite um n�mero:"))

n = eval(input("digite outro n�mero:"))

soma = 0

print("entre esses dois n�meros est�o:")

for i in range(N+1,n):

	print(i)
	soma = soma + i 
	soma = soma
print("a soma desses n�meros � igual a",soma)