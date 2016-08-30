n = eval(input("exibir a série de Fibonacci até o termo número:"))

def fib(n):

	a,b = 1,1

	for j in range(n):

		print(a)

		c = a + b

		a,b = b,c


fib(n)