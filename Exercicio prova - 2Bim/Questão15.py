n = eval(input("exibir a s�rie de Fibonacci at� o termo n�mero:"))

def fib(n):

	a,b = 1,1

	for j in range(n):

		print(a)

		c = a + b

		a,b = b,c


fib(n)